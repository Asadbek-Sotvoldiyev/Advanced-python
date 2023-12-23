def count_vowel(word):
    n = 0
    for i in word:
        if i in "aeiou":
            n+=1
    return n

def count_vowel_arr(arr):
    cnt = []
    for i in arr:
        cnt.append(count_vowel(i))
    a = list(filter(lambda x: x if max(cnt)==count_vowel(x) else 0, arr))
    return a,count_vowel(a[0])

print(count_vowel_arr(['hello', 'world', 'salom', 'dunyo']))
#Natija (['hello', 'salom', 'dunyo'], 2)
