def count_text(text):
    with open(text, "r") as file:
        f = file.read()
        return len(f.split())

print(count_text("my_text.txt"))
# result: 5