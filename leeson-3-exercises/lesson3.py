def max_char(text):
    text_list = list(text)
    char_counts = [text.count(i) for i in text]
    max_chars = []
    for i in text:
        if text.count(i)==max(char_counts):
            max_chars.append(i)
    return max_chars

print(max_char("Asadbek Sotvoldiyev"))