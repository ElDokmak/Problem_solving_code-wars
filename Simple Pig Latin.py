def pig_it(text):
    text = text.split()
    res = ''
    for i in range(len(text)):
        if len(text[i]) == 1:
            if i == len(text) - 1:
                new_word = text[i]
            else:
                new_word = text[i] + 'ay'
        else:
            letter_1 = text[i][0]
            new_word = text[i][1:] + letter_1 + 'ay'
        res = res + new_word + ' '
    return res[:-1]


print(pig_it('O tempora o mores !'))
