def square_digits(num):
    res = 0
    num = str(num)
    for i in range(len(num)):
        res = str(res) + str((int(num[i]))**2)
    return int(res[1:])


print(square_digits(2112))
