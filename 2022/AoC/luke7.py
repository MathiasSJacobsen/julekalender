class Directory:
    def __init__(self, name, parrent):
        self.name = name
        self.parrent = parrent
        self.directorys = []
        self.files = []

    def add_directory(self, child):
        self.directorys.append(child)

    def add_file(self, file):
        self.files.append(file)

    def get_directory(self, name):
        for child in self.directorys:
            if child.name == name:
                return child
        return None

    def get_file(self, name):
        for file in self.files:
            if file.name == name:
                return file
        return None

    def findDirectory(self, dirName):
        for dir in self.directorys:
            if dir.name == dirName:
                return dir
        return None

    def getSize(self):
        total = 0
        for file in self.files:
            total += file.size
        for dir in self.directorys:
            total += dir.getSize()
        return total

    def __str__(self):
        return f' - {self.name} (dir) \n\t - {self.directorys}\n\t - {self.files}'

    def __repr__(self):
        return f'{self.name} (dir)\n\t{self.files}'

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f'{self.name} (file, size={self.size})'

    def __str__(self):
        return f'{self.name} (file, size={self.size})'

def readFile(filepath):
    with open(filepath, 'r') as file:
        return [e.strip() for e in file.readlines()]

def parseFileContent(lst):
    root = Directory('/', None)
    currentDir = root
    ls = False
    for line in lst[1:]:
        if line[-2:] == '..':
            currentDir = currentDir.parrent
        elif line[0] == '$' and line[2:4] == 'cd':
            dir = Directory(line[5:], currentDir)
            currentDir = currentDir.add_directory(dir)
            currentDir = dir
        elif line[0] == '$' and line[2:4] == 'ls':
            ls = True
        elif line[:3] == 'dir':
            continue
        else:
            size, name = line.split()
            currentDir.add_file(File(name, int(size)))

    return root

def findAtMostSize(root: Directory, size: int):
    sizes = findSizeOfEachDirectory(root)
    s = 0
    for _, si in sizes:
        if si <= size:
            s += si
    return s

def findSizeOfEachDirectory(root: Directory):
    sizes = []
    dirs = [e for e in root.directorys]
    for dir in dirs:
        dirs.extend([e for e in dir.directorys])
        sizes.append((dir.name, dir.getSize()))
    return sizes


def part2(root):
    t = 30000000 - (70000000-root.getSize())
    sizes = findSizeOfEachDirectory(root)
    return min([e[1] for e in sizes if e[1] >= t])



if __name__ == '__main__':
    file = readFile('2022/AoC/luke7.txt')
    root = parseFileContent(file)
    print('Part 1: ', findAtMostSize(root, 100000))
    print('Part 2: ', part2(root)) 
