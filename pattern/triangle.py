def printTriangle(n):
    for i in range(n):
        st = ''
        for _ in range(n - (i + 1)):
            st += " "
        for _ in range(2 * (i + 1) - 1):
            st += '*'
        print(st)


if __name__ == '__main__':
    printTriangle(3)
    printTriangle(4)
    printTriangle(5)
    printTriangle(6)
