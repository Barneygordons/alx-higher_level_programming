#!/usr/bin/python3
""" write a file"""

python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'

def write_file(filename="", text=""):
    n = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
