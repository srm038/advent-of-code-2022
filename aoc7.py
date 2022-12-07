with open('7.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def getDir(dic, dirs):
    for dir in dirs:
        if not dir:
            continue
        dic = dic[dir]
    return dic


def parseTree(input):
    fileSystem = {'/': {}}
    folders = {'/'}
    for i, line in enumerate(input):
        if '$ ' in line:
            if 'cd /' in line:
                curr = ['/']
                ls = False
            elif 'cd ..' in line:
                curr = curr[:-1]
            elif 'cd ' in line:
                curr.append(line.split(' ')[2])
        else:
            if 'dir' in line:
                dir = line.split(' ')[1]
                getDir(fileSystem, curr).update({dir: {}})
                folders.add('/'.join(curr + [dir]))
            else:
                size, name = line.split(' ')
                getDir(fileSystem, curr).update({name: int(size)})
    return fileSystem, folders


def getDirSize(fileSystem, dir):
    total = 0
    cwd = getDir(fileSystem, ['/'] + dir[1:].split('/'))
    for i in cwd:
        if isinstance(cwd[i], int):
            total += cwd[i]
        else:
            total += getDirSize(fileSystem, dir + '/' + i)
    return total


fileSystem, folders = parseTree(input)

print(sum(filter(lambda i: i <= 100000, [getDirSize(fileSystem, dir) for dir in folders])))

min([dir for dir in folders if getDirSize(fileSystem, dir) >= 30000000 - (70000000 - getDirSize(fileSystem, '/'))], key=lambda dir: getDirSize(fileSystem, dir))