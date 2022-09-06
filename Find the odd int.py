def find_it(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        times = 0
        for i in range(0, len(numbers)):

            for j in range(0, len(numbers)):
                if numbers[j] == numbers[i]:
                    times = times + 1
            if times % 2 != 0:
                return(numbers[i])
            times = 0


print(find_it([18, 18, 18, 18, 18]))
