# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?".
# Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A),
# and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0).
# Note that the non-alphanumeric characters remain unchanged.
import string


class Solution:
    def rotationalCipher(self, input, rotation_factor):
        letters = list(string.ascii_lowercase)
        table = {v: i for i, v in enumerate(letters)}
        cipher = ''
        number_r = rotation_factor % 10
        letter_r = rotation_factor % 26

        for c in input:
            if c.isnumeric() and number_r:
                # 10 numbers
                cipher += str((int(c) + number_r) % 10)
            elif c.isalpha() and letter_r:
                cap = c.isupper()
                c = c.lower()
                # 26 letters
                r = (letter_r + table[c]) % 26
                if cap:
                    cipher += letters[r].upper()
                else:
                    cipher += letters[r]
            else:
                cipher += c
        return cipher


s = Solution()
t = 'Zebra-493?'
a = s.rotationalCipher(t, 3)
# Cheud-726?
print(a)
