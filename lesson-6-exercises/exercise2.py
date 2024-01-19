def count_vowel(word):
    count = 0
    vowels = "aeiouAEIOU"
    for i in word:
        if i in vowels:
            count+=1
    return count
def max_vowels(arr):
    count_vowels = []
    max_vowel = []
    for i in arr:
        count_vowels.append(count_vowel(i))
    for i in arr:
        if count_vowel(i)==max(count_vowels):
            max_vowel.append(i)
    return max_vowel, max(count_vowels)    

print(max_vowels(['hello', 'salom', 'world']))
    