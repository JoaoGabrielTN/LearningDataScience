#!/usr/bin/env python3
import os
import re

line = ''
content = []
currentDirectory = os.getcwd()
dataDirectory = currentDirectory + "/DataProcessing/data"

for filename in os.listdir(dataDirectory):
    i = 0
    with open(os.path.join(dataDirectory, filename), 'r') as f:
        text = f.read()
        while i < len(text):
            if text[i] == 'U' and text[i+1] == 'R' and text[i+2] == 'L':
                break
            line = line + text[i]
            i += 1
        content.append(line)
        line = ''
                

for i in content:
    print(i)
        

