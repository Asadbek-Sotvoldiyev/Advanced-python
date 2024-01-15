def polindrome_number(num):
    if num>0:
        if num==int(str(num)[::-1]):
            return True
        else:
            return False
    else:
        return False

print(polindrome_number(121))
# result: True