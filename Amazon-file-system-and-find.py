# file and directory system OOP
# file system is like a n-ary tree where each node is
# either a directory or a file. In fact files should be leaves
# root is root directory
from datetime import datetime
from sys import maxsize
from typing import List


# base class for file system
class Entry:
    def __init__(self, name: str):
        self.name = name
        self.created = datetime.now()
        self.lastUpdate = datetime.now()
        self.lastAccess = None
        self.size = 0


class Directory(Entry):
    # have subEntries, superEntry
    def __init__(self, name: str, superEntry: Entry, subEntries: {str: Entry} = {}):
        super().__init__(name)
        self.superEntry = superEntry
        self.subEntries = subEntries


class File(Entry):
    # have type and content
    def __init__(self, name: str, type: str, content: str):
        super().__init__(name)
        self.type = type
        self.content = content


class SearchCriterion:
    def meet(self, entry: Entry) -> bool:
        # define the logic here
        # return True if entry meets the search criterion
        # return False if entry does NOT meet the search criterion
        pass


class SearchBySize(SearchCriterion):
    def __init__(self, lowerBound: int = 0, upperBound: int = maxsize):
        if lowerBound > upperBound:
            raise ValueError('lower bound must be less than or equal to upper bound.')
        self.lowerBound = max(0, lowerBound)
        self.upperBound = min(maxsize, upperBound)

    def meet(self, entry: Entry) -> bool:
        if not entry:
            return False
        return self.lowerBound < entry.size < self.upperBound


class SearchByType(SearchCriterion):
    def __init__(self, include: List[str] = []):
        self.include = set(include)

    def addFileType(self, type: str):
        if type:
            self.include.add(type)

    def removeFileType(self, type: str):
        if type:
            self.include.discard(type)

    def meet(self, f: File) -> bool:
        if not f:
            return False
        return f.type in self.include


class FileSystem:
    DIR_SEPARATOR = '/'

    def __init__(self):
        self.rootDirectory = Directory('root', None)
        self.curDirectory = self.rootDirectory
        self.curPath = self.DIR_SEPARATOR + self.root.name

    def findFiles(self, under: Directory, criteria: List[SearchCriterion] = [], recursively: bool = True) -> List[File]:
        if not under:
            raise ValueError('Invalid directory, please check and retry.')
        files = []
        self.__dfsFiles(under, criteria, recursively, files)
        return files

    def goTo(self, path: str):
        entry = self.self.__getEntry(path)
        if not entry:
            print(f'Can\'t find path \'{path}\', please check and retry.')
            return
        self.__accessEntry(entry)
        self.curDirectory = entry
        self.curPath = self.__formatPath(path)
        if self.__isFile(entry):
            self.goUp()

    def goUp(self):
        if self.curDirectory == self.rootDirectory:
            return
        self.curPath = self.curPath[:-len(self.curDirectory.name)]
        self.curDirectory = self.curDirectory.superEntry
        self.__accessEntry(self.curDirectory)

    def isFile(self, path: str) -> bool:
        entry = self.__getEntry(path)
        if not entry:
            print(f'Can\'t find path \'{path}\', please check and retry.')
            return False
        return self.__isFile(entry)

    def isDirectory(self, path: str) -> bool:
        entry = self.__getEntry(path)
        if not entry:
            print(f'Can\'t find path \'{path}\', please check and retry.')
            return False
        return self.__isDirectory(entry)

    def __dfsFiles(self, curDir: Directory, criteria: List[SearchCriterion], recursively: bool, files: List[File]):
        # base case, empty folder
        if not curDir.subEntries:
            return
        for subEntry in curDir.subEntries:
            if self.__isFile(subEntry):
                # check the file against all criteria
                include = True
                for criterion in criteria:
                    # if one fails, no need to check more criteria
                    if not criterion.meet(subEntry):
                        include = False
                        break
                if include:
                    files.append(subEntry)
            else:
                # keep dfs
                if recursively:
                    self.__dfsFiles(subEntry, criteria, recursively, files)

    def __isFile(self, entry: Entry) -> bool:
        if not entry:
            return False
        return isinstance(entry, File)

    def __isDirectory(self, entry: Entry) -> bool:
        if not entry:
            return False
        return isinstance(entry, Directory)

    def __getEntry(self, path: str) -> Entry:
        path = self.__formatPath(path)
        if not path:
            return None
        names = path.split(self.DIR_SEPARATOR)
        # remove file type if any
        i = names[-1].find('.')
        if i != -1:
            names[-1] = names[-1][:i]
        # find entry
        if names[0] != 'root':
            return None
        entry = self.rootDirectory
        for i in range(2, len(names)):
            entry = entry.subEntries.get(names[i], None)
            if not entry:
                return None
        return entry

    def __formatPath(self, path: str) -> str:
        formatPath = path
        if formatPath[0] != self.DIR_SEPARATOR:
            formatPath = self.DIR_SEPARATOR + formatPath
        if formatPath[-1] == self.DIR_SEPARATOR:
            formatPath = formatPath[:-1]
        return formatPath

    def __getPath(self, entry: Entry) -> str:
        if not entry:
            return ''
        names = []
        cur = entry
        while cur:
            names.append(cur.name)
            cur = cur.superEntry
        return self.DIR_SEPARATOR + self.DIR_SEPARATOR.join(names)

    def __accessEntry(self, entry: Entry):
        if not entry:
            return
        if self.__isFile(entry):
            print(f'Opening file \'{entry.name}.{entry.type}\'...')
            print(entry.content)
        entry.lastAccess = datetime.now()
