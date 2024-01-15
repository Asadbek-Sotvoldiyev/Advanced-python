def reverse_string(strng):
    str_list = strng.split()[::-1]
    for i in range(len(str_list)):
        str_list[i] = str_list[i][::-1]
    return " ".join(str_list)

print(reverse_string("the sky is blue"))
