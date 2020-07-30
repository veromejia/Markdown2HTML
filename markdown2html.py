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

    my_mdfile = sys.argv[1]
    my_dict = {"#": "h1", "##": "h2", "###": "h3",
               "####": "h4", "#####": "h5", "######": "h6"}

    name, exten = os.path.splitext(my_mdfile)
    if (not os.path.exists(my_mdfile) or not exten == ".md"):
        print("Missing {}".format(my_mdfile), file=sys.stderr)
        exit(1)

    with open(my_mdfile, 'r') as mdfile, open(sys.argv[2], 'w') as htmlfile:
        for line in mdfile:
            headings = line.split(" ", 1)[0]
            new_line = (line.split(" ", 1)[1]).rstrip('\n')
            count = len(headings)
            for key, val in my_dict.items():
                if headings == key:
                    htmlfile.write("<{}>{}</{}>\n".format(val, new_line, val))
    exit(0)
