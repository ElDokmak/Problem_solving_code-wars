def rgb(r, g, b):
    numbers = [r, g, b]
    final = ''
    for i in range(len(numbers)):
        if numbers[i] > 255:
            numbers[i] = 255
        if numbers[i] < 0:
            numbers[i] = 0
    for j in range(len(numbers)):
        res = hex(numbers[j])[2:]
        if len(res) == 1:
            res = '0' + res
        final = final + res
    return(final.upper())


print(rgb(-20, 275, 125))
