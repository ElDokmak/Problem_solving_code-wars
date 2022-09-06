def high_and_low(numbers):
    res = ''
    numbers = numbers.split(' ')
    max = int(numbers[0])
    min = int(numbers[0])
    for i in range(len(numbers)):
        if int(numbers[i]) > max:
            max = int(numbers[i])
        if int(numbers[i]) < min:
            min = int(numbers[i])
    res = str(max) + ' ' + str(min)
    return res


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
