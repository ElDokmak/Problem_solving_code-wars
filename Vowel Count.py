def get_count(word):
    vowels = ['a', 'e', 'i', 'u', 'o']
    times = 0
    for i in range(len(word)):
        for j in range(len(vowels)):
            if word[i] == vowels[j]:
                times = times + 1
    return times


print(get_count("ahmed eldokmak"))
