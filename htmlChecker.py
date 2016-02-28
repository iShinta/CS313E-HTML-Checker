#  File: htmlChecker.py
#  Description: Verifies in HTML file if tags are correctly matched
#  Student's Name: Minh-Tri Ho
#  Student's UT EID: mh47723
#  Course Name: CS 313E
#  Unique Number: 50940
#
#  Date Created: 02/28/16
#  Date Last Modified: 02/28/16

import stack

#Returns the tags inside a list
def getTag(text):
    res = []
    tags_marker = "<>"
    tag_open = False

    for i in range(len(text)):
        if(text[i] == tags_marker[0]):
            if(tag_open == True):
                print("[Error]: Tag already opened")
            else:
                tag_open = True
                tag = ""
        elif(text[i] == tags_marker[1]):
            if(tag_open == False):
                print("[Error]: Closing Tag without opening one")
            else:
                tag_open = False
                res.append(tag)
                #[DEBUG]print("Added tag:",tag)
        else:
            if(tag_open == True):
                tag += (text[i])

    return res

def main():
    file_name = "htmlfile.txt"
    html_file = open('./' +file_name, 'r')

    text = html_file.read()
    tag_list = getTag(text)

    print(tag_list)

main()
