#coding=utf-8
import os
def txtWrite():
    path = u"E:\\test"
    with open("F:\\txtWrite\\txtWrite.txt", "w") as f:
        for (root,dirs,files) in os.walk(path):
            for name in files:
                #if name.endswith(".jpg"):
                    i = os.path.join(root, name)
                    print(i)
                    f.write(i.encode('gb2312')+'\n')

if __name__ == '__main__':
    txtWrite()