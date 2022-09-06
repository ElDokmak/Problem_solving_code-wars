# accum("cwAt") -> "C-Ww-Aaa-Tttt"
def accum(word):
    new = ''
    res = ''
    for i in range(len(word)):

        if word[i] == word[i].upper():
            new = word[i]
            new = new + i*word[i].lower() + "-"

        else:
            new = word[i].capitalize()
            new = new + i*word[i] + "-"
        res = res + new
    return res[:-1]


op = accum("cwAt")
print('"' + op + '"')
