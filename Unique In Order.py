def unique_in_order(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0]]
    else:

        new_list = []
        previous = None
        for item in arr:
            if item != previous:
                new_list.append(item)
            previous = item
        return new_list


print(unique_in_order('AAAABBBCCDAABBB'))
