def difference_str(str1, str2):
    n = ''
    for i in str1:
        if i not in str2:
            n+=i
    return n

print(difference_str('abcde', 'abcd'))