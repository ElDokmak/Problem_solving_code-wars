def find_missing_letter(letters):
    for i in range(ord(letters[0]), ord(letters[len(letters)-1])):
        # [79 , 81 , 82 ,83]
        for j in range(len(letters)):
            # ['O','Q','R','S']
            if letters[j] != chr(i+j):
                # Q != 80 TRUE MISSING LETTER chr(80)
                return chr(i+j)


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
