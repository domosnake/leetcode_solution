from random import choices, sample, seed
from typing import List, Dict
from string import ascii_letters, digits


class SubstitutionUnit:
    def __init__(self, alphabet: str, batch: int):
        self._abc = alphabet
        # Ensure identical settings within a batch
        self._batch = batch
        if batch > 0:
            seed(batch)

    def forward(self, i: int) -> int:
        """
        Map plain text index to cipher text index.
        """
        pass

    def backward(self, i: int) -> int:
        """
        Map cipher text index to plain text index.
        """
        pass


class Plugboard(SubstitutionUnit):
    def __init__(self, alphabet: str, batch: int):
        super().__init__(alphabet, batch)
        self._map = {}

    def plug(self, i1: int, i2: int):
        if i1 == i2:
            raise ValueError('Plugs must be different')
        if i1 in self._map:
            raise ValueError(f'Plug {self._abc[i1]} in use')
        if i2 in self._map:
            raise ValueError(f'Plug {self._abc[i2]} in use')
        self._map[i1] = i2
        self._map[i2] = i1

    def unplug(self, i1: int, i2: int):
        if i1 not in self._map:
            raise ValueError(f'Plug {self._abc[i1]} not found')
        if i2 not in self._map:
            raise ValueError(f'Plug {self._abc[i2]} not found')
        if i2 != self._map[i1]:
            raise ValueError(
                f'Plugs {self._abc[i1]} and {self._abc[i2]} not in pairs')
        del self._map[i1]
        del self._map[i2]

    def unplug_all(self):
        self._map.clear()

    def forward(self, i: int) -> int:
        return self._map.get(i, i)

    def backward(self, i: int) -> int:
        return self.forward(i)


class Reflector(SubstitutionUnit):
    def __init__(self, alphabet: str, batch: int, encrypt_to_self: bool):
        super().__init__(alphabet, batch)
        self._map = {}
        s = len(alphabet)
        if encrypt_to_self:
            pool = [n for n in range(s)]
            while pool:
                # Choose 2 randomly with repetition
                i1, i2 = choices(pool, k=2)
                self._map[i1] = i2
                self._map[i2] = i1
                pool.remove(i1)
                if i1 != i2:
                    pool.remove(i2)
        else:
            shuffled = sample(range(s), s)
            for i in range(1, s, 2):
                self._map[shuffled[i]] = shuffled[i - 1]
                self._map[shuffled[i - 1]] = shuffled[i]

    def forward(self, i: int) -> int:
        return self._map.get(i, i)

    def backward(self, i: int) -> int:
        return self.forward(i)


class Rotor(SubstitutionUnit):
    def __init__(self, alphabet: str, batch: int):
        super().__init__(alphabet, batch)
        self._pos = 0
        self._size = len(alphabet)
        # Wire contacts randomly
        self._forward_map = sample(range(self._size), self._size)
        self._backward_map = [0] * self._size
        for i, v in enumerate(self._forward_map):
            self._backward_map[v] = i

    @property
    def pos(self) -> int:
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    def rotate(self) -> bool:
        carry = (self._pos + 1) >= self._size
        self._pos = (self._pos + 1) % self._size
        return carry

    def forward(self, i: int) -> int:
        ii = (i + self._pos) % self._size
        j = self._forward_map[ii]
        jj = (j - self._pos) % self._size
        return jj

    def backward(self, i: int) -> int:
        ii = (i + self._pos) % self._size
        j = self._backward_map[ii]
        jj = (j - self._pos) % self._size
        return jj


class Enigma:
    """
    恩尼格玛机是一种排己，自反，多字母替换表的密码机。
    基本结构为一套键盘以及对应每个键位的灯泡，一个接线板，若干个转子和一个反射器。
    当按下键盘上某一个字母，信号经过接线板映射，转子，反射板反射；再经过转子，接线板，最后点亮某个键位的灯泡完成加解密。

    Note:
        二战中恩尼格玛机的排己性是其一大弊端，所以代码实现为其添加了可选参

    Args:
        alphabet (str): 字母表
        batch (int): 同一批次（正整数）产品内部接线完全一致，默认为0，即每个实例接线随机
        rotor_size (int): 转子数量，默认为3
        encrypt_to_self (bool): 反射板是否排己，默认为False，即明文不可能被加密为明文本身

    Properties:
        batch (int): 产品批次
        rotor_positions (List[int]): 转子当前位置
        plugs (Dict[str, str]): 接线字母对

    Methods:
        init_rotor_positions: 初始化转子起始位置，加解密需要转子起始位置一致
        plug: 连接某两个字母
        plug_all: 连接所有指定字母对
        unplug: 断开字母对连接
        unplug_all: 断开所有接线
        encrypt: 加密明文
        decrypt: 解密密文
    """
    def __init__(self,
                 alphabet: str,
                 batch: int = 0,
                 rotor_size: int = 3,
                 encrypt_to_self: bool = False):
        if not alphabet:
            raise ValueError('Alphabet must be provided')
        if len(set(alphabet)) != len(alphabet):
            raise ValueError('Alphabet must be unique')
        if rotor_size <= 0:
            raise ValueError('Rotor size must be positive')
        self._abc = ''.join(sorted(alphabet))
        self._map = {
            k: v
            for i, c in enumerate(self._abc) for k, v in {
                i: c,
                c: i
            }.items()
        }
        self._plugs = {}
        self._batch = batch
        # Build components
        self._rotors = self._build_rotors(rotor_size)
        self._reflector = self._build_reflector(encrypt_to_self)
        self._plugboard = self._build_plugboard()

    @property
    def batch(self) -> int:
        return self._batch

    @property
    def rotor_positions(self) -> List[int]:
        return [r.pos for r in self._rotors]

    @property
    def plugs(self) -> Dict[str, str]:
        return self._plugs

    def init_rotor_positions(self, positions: List[int]):
        if not positions or len(positions) != len(self._rotors):
            raise ValueError('Invalid rotor positions')
        for i, v in enumerate(positions):
            if v < 0 or v >= len(self._abc):
                raise ValueError(f'Invalid rotor position {v}')
            self._rotors[i].pos = v

    def plug(self, c1: str, c2: str):
        self._validate_text(f'{c1}{c2}')
        self._plugboard.plug(self._map[c1], self._map[c2])
        self._plugs[c1] = c2

    def unplug(self, c1: str, c2: str):
        self._validate_text(f'{c1}{c2}')
        self._plugboard.unplug(self._map[c1], self._map[c2])

    def plug_all(self, pairs: Dict[str, str]):
        for c1, c2 in pairs.items():
            self.plug(c1, c2)

    def unplug_all(self):
        self._plugboard.unplug_all()
        self._plugs.clear()

    def encrypt(self, plaintext: str) -> str:
        self._validate_text(plaintext)
        ciphertext = []
        for c in plaintext:
            i = self._map[c]
            j = self._encode(i)
            self._rotate()
            ciphertext.append(self._map[j])
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)

    def _build_rotors(self, rotor_size: int) -> List[Rotor]:
        return [Rotor(self._abc, self._batch + i) for i in range(rotor_size)]

    def _build_reflector(self, self_reflecting: bool) -> Reflector:
        return Reflector(self._abc, self._batch, self_reflecting)

    def _build_plugboard(self) -> Plugboard:
        return Plugboard(self._abc, self._batch)

    def _rotate(self):
        for rotor in self._rotors:
            carry = rotor.rotate()
            if not carry:
                return

    def _encode(self, i: int) -> str:
        j = -1
        # Plugboard
        j = self._plugboard.forward(i)
        i = j
        # Rotors forward
        for rotor in self._rotors:
            j = rotor.forward(i)
            i = j
        # Reflect
        j = self._reflector.forward(i)
        i = j
        # Rotors backward
        for rotor in reversed(self._rotors):
            j = rotor.backward(i)
            i = j
        # Plugboard
        j = self._plugboard.backward(i)
        return j

    def _validate_text(self, text: str):
        for c in text:
            if c not in self._map:
                raise ValueError(f'Invalid character {c}')


def test_enigma():
    # init objects
    alpha = f'{ascii_letters}{digits} ,.!'
    batch = 0
    rotor_size = 3
    pos = [0, 2, 1]
    plaintext = 'Hello AMAZING world!'
    plugs = {'k': 'a', 'n': 'o', 'p': 'x', 'z': 'm'}

    # create enigma
    ww2_enigma = Enigma(alpha, batch, rotor_size)
    print(f'Enigma created: batch - {batch}, rotors - {rotor_size}')

    # set plugs, thus chars in paris are mapped to eath other
    ww2_enigma.plug_all(plugs)
    print(f'Set plugs: {plugs}\n')

    # plain to cipher
    ww2_enigma.init_rotor_positions(pos)
    print(f'Roter positions set to： {pos}, encrypting...')
    ciphertext = ww2_enigma.encrypt(plaintext)
    print(f'Encrypted: {plaintext} -> {ciphertext}\n')

    # cipher to plain
    ww2_enigma.init_rotor_positions(pos)
    print(f'Roter positions set to： {pos}, decrypting...')
    plaintext = ww2_enigma.decrypt(ciphertext)
    print(f'Decrypted: {ciphertext} -> {plaintext}')


if __name__ == '__main__':
    test_enigma()
