import random
def son_top(num):
    count = 0
    n = random.randint(1, 50)
    while True:
        count+=1
        if n==num:
            return count
        elif n>num:
            num = int(input(f"Men o'ylagan son bundan kattaroq, qayta kiriting: "))
        else:
            num = int(input(f"Men o'ylagan son bundan kichikroq, qayta kiriting: "))
num = int(input("Men 1-50 oralig'ida bir son o'yladim topib ko'ringchi: "))
a = son_top(num)
if a<3:
    print(f"Qoil, siz {a} urinishda topdingiz bu judayam a'lo natija.")
elif a<=5:
    print(f"Tabrilaymiz, siz {a} urinishda topdingiz bu o'rtacha natija.")
else:
    print(f"Yaxshi, siz {a} urinishda topdingiz bu eng yomon natija.")




