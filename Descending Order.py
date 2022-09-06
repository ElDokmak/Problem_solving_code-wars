def Descending_Order(num):
    stringedNum = str(num)
    listedNum = list(stringedNum)
    sortedList = sorted(listedNum)
    stringedNum = ''.join(sortedList)
    num = int(stringedNum[:: -1])
    return num


print(Descending_Order(1548))
