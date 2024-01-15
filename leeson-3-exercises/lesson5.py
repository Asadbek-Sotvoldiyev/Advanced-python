def my_index(text, element):
    for i in range(len(text)):
        if text[i]==element:
            return i
    raise IndexError('Bunday element mavjud emas!!!')

print(my_index('Asadbek', "d"))
# result: 3