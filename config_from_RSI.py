import re
import os
#read RSI file
print("reading RSI file")

f = open('/Users/eamin/Downloads/RSI.txt')
f = open('/Users/eamin/Downloads/RSI.txt')
fo = open('/Users/eamin/Downloads/config_from_RSI.txt','w')
myflag = False
for lines in f:
    #lines = f.readlines()
    matchObj = re.search(r'show configuration', lines)
    #print(lines)
    #print(matchObj)
    if(matchObj):
        #print(lines)
        fo.write(lines)
        myflag = True
    elif(myflag):
        #print(lines)
        fo.write(lines)
        matchObj2 = re.search (r'show', lines)
        if(matchObj2):
            break
    else:
        continue 

print('config extraction is complete')
