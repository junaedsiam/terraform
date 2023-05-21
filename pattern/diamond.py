def printDiamond(n):
    for i in range(n):
        st = ''
        for _ in range(n - (i + 1)):
            st += " "
        for _ in range(i + 1):
            st += '* '
        print(st)

    for i in range(n, 0, -1):
        st = ""
        for _ in range(n - i):
            st += ' '
        for _ in range(i):
            st += '* '
        print(st)


if __name__ == '__main__':
    printDiamond(3)
    printDiamond(4)
    printDiamond(5)
    printDiamond(6)
