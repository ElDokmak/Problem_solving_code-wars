def solution(string, ending):
    x = len(ending)
    if x == 0:
        return True
    if string[-x:] == ending:
        return True
    else:
        return False


print(solution("abc", ""))
