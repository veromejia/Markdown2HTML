#!/usr/bin/python3
"""script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name"""


import sys
import os.path

if __name__ == '__main__':
    my_dict = {"#": "h1", "##": "h2", "###": "h3", "####": "h4",
               "#####": "h5", "######": "h6", "-": "ul", "*": "ol"}
    isOpeningUlTag = False
    isOpeningOlTag = False

    if (len(sys.argv) <= 2):
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    my_mdfile = sys.argv[1]
    name, exten = os.path.splitext(my_mdfile)
    if (not os.path.exists(my_mdfile) or not exten == ".md"):
        print("Missing {}".format(my_mdfile), file=sys.stderr)
        exit(1)

    with open(my_mdfile, 'r') as mdfile:
        with open(sys.argv[2], 'w') as htmlfile:
            for line in mdfile:
                headings = line.split(" ", 1)[0]
                if headings in my_dict.keys():
                    new_line = (line.split(" ", 1)[1]).rstrip('\n')
                    for key, val in my_dict.items():
                        if headings == key:
                            if "#" in headings:
                                if isOpeningUlTag:
                                    isOpeningUlTag = False
                                    htmlfile.write("</ul>\n")
                                if isOpeningOlTag:
                                    isOpeningOlTag = False
                                    htmlfile.write("</ol>\n")

                                htmlfile.write(
                                    "<{}>{}</{}>\n".format(val, new_line, val))
                            elif "-" in headings:
                                if isOpeningOlTag:
                                    isOpeningOlTag = False
                                    htmlfile.write("</ol>\n")

                                if isOpeningUlTag is False:
                                    isOpeningUlTag = True
                                    htmlfile.write("<{}>\n".format(val))
                                htmlfile.write(
                                    "\t<li>{}</li>\n".format(new_line))
                            elif "*" in headings:
                                if isOpeningUlTag:
                                    isOpeningUlTag = False
                                    htmlfile.write("</ul>\n")

                                if isOpeningOlTag is False:
                                    isOpeningOlTag = True
                                    htmlfile.write("<{}>\n".format(val))
                                htmlfile.write(
                                    "\t<li>{}</li>\n".format(new_line))

                            else:
                                if isOpeningUlTag:
                                    isOpeningUlTag = False
                                    htmlfile.write("</ul>\n")
                                if isOpeningOlTag:
                                    isOpeningOlTag = False
                                    htmlfile.write("</ol>\n")

            if isOpeningUlTag:
                isOpeningUlTag = False
                htmlfile.write("</ul>\n")
            if isOpeningOlTag:
                isOpeningOlTag = False
                htmlfile.write("</ol>\n")
    exit(0)
