import re

def count_word(text):
    with open(text, "r") as file:
        f = file.readlines()
        
    result = re.findall("\w+", f[0])
    return len(result)

print(count_word('lesson-6-exercises/text.txt'))