def get_sum(a, b):
    sum = 0
    if a == b:
        sum = a
    elif a > b:
        for i in range(b, a+1):
            sum = sum + i
    else:
        for i in range(a, b+1):
            sum = sum + i
    return sum


print(get_sum(17, 17))
