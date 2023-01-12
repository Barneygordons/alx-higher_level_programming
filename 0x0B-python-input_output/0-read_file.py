#!/usr/bin/python3
""" read a file """

python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'

def read_file(filename=""):
    with open(filename,  encoding='utf-8') as f:
        print(f.read(), end="")
