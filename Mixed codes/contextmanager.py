from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        return f
    finally:
        f.close()
        
with open_file("sample.txt", "r") as file:
    file.read()