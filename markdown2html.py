#!/usr/bin/python3
"""script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name"""


import sys
import os.path

if __name__ == '__main__':
    if (len(sys.argv) <= 2):
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    my_file = sys.argv[1]
    name, exten = os.path.splitext(sys.argv[1])
    if (os.path.exists(sys.argv[1]) and exten == ".md"):
        exit(0)
    else:
        print("Missing:{}".format(my_file), file=sys.stderr)
        exit(1)
