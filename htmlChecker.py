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

def getStack(list):
    res = stack.Stack()

    for elt in list:
        if(elt[0] == '/'):
            if(elt[1:] == res.peek()):
                res.pop()
            else:
                print("[Error]: Mismatch. Tag is",elt[1:],"but top of stack is",res.peek())
        else:
            if(not(elt in validtags)):
                validtags.append(elt)

            #Check for exceptions
            if(elt[:4] == "meta"):
                print("META tag found")
            elif(elt[:2] == "br"):
                print("BR tag found")
            elif(elt[:2] == "hr"):
                print("HR tag found")
            else:
                res.push(elt)

    return res

def main():
    file_name = "htmlfile.txt"
    html_file = open('./' +file_name, 'r')

    text = html_file.read()
    tag_list = getTag(text)
    #[DEBUG]print(tag_list)
    global validtags
    validtags = []
    tag_stack = getStack(tag_list)

    #Summary
    if(tag_stack == []):
        print("Processing complete. No mismatches found.")
    else:
        print("Processing complete. Unmatched tags remain on stack:", tag_stack)

main()
