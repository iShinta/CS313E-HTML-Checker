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

def main():
    file_name = "htmlfile.txt"
    html_file = open('./' +file_name, 'r')

    #Where the tags are stored in order
    tags = stack.Stack()
    tags_marker = "<>"

    #Initialization of checker variables
    tag_open = False

    for line in html_file:

        #Extracts the tags
        for i in range(len(line)):
            if(line[i] == tags_marker[0]):
                if(tag_open == True):
                    print("[Error]: Tag already opened")
                else:
                    tag_open = True
                    tag = ""
            elif(line[i] == tags_marker[1]):
                if(tag_open == False):
                    print("[Error]: Closing Tag without opening one")
                else:
                    tag_open = False
                    tags.push(tag)
                    print("Added tag:",tag)
            else:
                if(tag_open == True):
                    tag += (line[i])


main()
