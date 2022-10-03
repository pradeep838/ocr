import json

# jsonStr = {"script":"#!/bin/bash echo Hello World"}

# j = json.loads(jsonStr)
# text='{"From Files and Folders.":[130, 92, 0, 0]}'
# text=json.loads(text)
# print(text)
# exit()
def kbread(text):
    container={}
    with open('kb.json','r') as f:
        content=f.read()
        print(content)
        if content.strip()=="":
            pass
        else:
            container=json.loads(content)
    # container=json.load('kb.')
    if not container.get(text)==None:return container[text]
    else: return  -1

# print(kbread('From Files and Folders.'))
# exit()

# str="this is some ' string hallo ' test file"
# print(str.replace("'",'"'))