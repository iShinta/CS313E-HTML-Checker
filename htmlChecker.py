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
                print("[ERROR]: Tag already opened")
            else:
                tag_open = True
                tag = ""
        elif(text[i] == tags_marker[1]):
            if(tag_open == False):
                print("[ERROR]: Closing Tag without opening one")
            else:
                tag_open = False
                res.append(tag)
                #[DEBUG]print("Added tag:",tag)
        else:
            if(tag_open == True):
                tag += (text[i])

    return res

def arbo(list):
    res = ""
    index = 0
    for elt in list:
        res += ("<" +elt +">")
        if(elt[0] == '/'):
            res += '\n'
    return res

def strList(list):
    res = ""
    index = 0
    for elt in list:
        res += ("<" +elt +">\n")
    return res

def getStack(list):
    res = stack.Stack()

    for elt in list:
        if(elt[0] == '/'):
            if(elt[1:] == res.peek()):
                res.pop()
                print("[STACK]", elt, "tag found and matched. Stack is now", res)
            else:
                print("[ERROR]: Mismatch. Tag is",elt[1:],"but top of stack is",res.peek())
        else:
            if(not(elt in validtags)):
                print("[TAGS]  Tag",elt,"not recognized. Adding to list.")
                validtags.append(elt)

            #Check for exceptions
            if(elt[:4] == "meta"):
                print("[STACK] META tag found. No need to match. Stack is still", res)
                if(not(elt in exceptions)):
                    print("[TAGS]  Tag",elt,"not recognized. Adding to list.")
                    exceptions.append(elt[:4])
            elif(elt[:2] == "br"):
                print("[STACK] BR tag found. No need to match. Stack is still", res)
                if(not(elt in exceptions)):
                    print("[TAGS]  Tag",elt,"not recognized. Adding to list.")
                    exceptions.append(elt[:2])
            elif(elt[:2] == "hr"):
                print("[STACK] HR tag found. No need to match. Stack is still", res)
                if(not(elt in exceptions)):
                    print("[TAGS]  Tag",elt,"not recognized. Adding to list.")
                    exceptions.append(elt[:2])
            else:
                res.push(elt)
                print("[STACK]", elt, "tag found and pushed. Stack is now", res)

    return res

def main():
    file_name = "htmlfile.txt"
    html_file = open('./' +file_name, 'r')

    text = html_file.read()
    tag_list = getTag(text)
    print("________________LIST________________")
    print(arbo(tag_list))

    global validtags
    validtags = []
    global exceptions
    exceptions = []
    print("________________STACK________________")
    tag_stack = getStack(tag_list)

    #Summary
    if(tag_stack == []):
        print("[RESULT] Processing complete. No mismatches found.")
    else:
        print("[RESULT] Processing complete. Unmatched tags remain on stack:", tag_stack)

    print("\n________________VALIDTAGS________________")
    print(strList(validtags))

    print("________________EXCEPTIONS________________")
    print(strList(exceptions))

main()
