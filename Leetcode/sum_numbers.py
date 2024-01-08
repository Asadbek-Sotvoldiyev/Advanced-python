def sum_nums(num):
    if num==0:
        return 0
    else:
        return num+sum_nums(num-1)


print(sum_nums(100))