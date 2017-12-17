#coding=utf-8
import os

with open(u'F:\\txtWrite\\txtWrite.txt','r') as f1 :
    files = f1.readlines()
    for lines in files:
        print lines

with open(u'F:\\txtWrite\\txtWrite2.txt','w') as f2 :
    for lines in files:
        f2.write(lines)

