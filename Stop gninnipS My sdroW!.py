def spin_words(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        if len(sentence[i]) >= 5:
            sentence[i] = sentence[i][::-1]
        else:
            sentence[i] = sentence[i]
    return ' '.join(sentence)


print(spin_words("This is another test"))
