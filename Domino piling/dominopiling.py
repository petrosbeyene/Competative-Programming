def dominoPiling(m, n):
        numOfDominos = (m*n) // 2
        return numOfDominos

inp = input()
inpList = inp.split()
print(dominoPiling(int(inpList[0]), int(inpList[1])))
