import os
import time
import threading
from time import ctime,sleep

def fileWirtekw():
    for i in range(0, 10000000, 1):
        fileName = str(i) + ".txt"
        fileNum = str(i%10+1)
        open("G:\\5kw\\" + fileNum + "\\" + fileName,"w")
        print("G:\\5kw\\" + fileNum + "\\" +fileName)

def fileWirte2kw():
    for j in range(10000000, 20000000, 1):
        fileName2 = str(j) + ".txt"
        fileNum2 = str(j%10+1)
        open("G:\\5kw\\" + fileNum2 + "\\" + fileName2, "w")
        print("G:\\5kw\\" + fileNum2 + "\\"  + fileName2)

def fileWirte3kw():
    for j in range(10000000, 20000000, 1):
        fileName3 = str(j) + ".txt"
        fileNum3 = str(j%10+1)
        open("G:\\5kw\\" + fileNum3 + "\\" + fileName3, "w")
        print("G:\\5kw\\" + fileNum3 + "\\"  + fileName3)

def fileWirte4kw():
    for j in range(10000000, 20000000, 1):
        fileName4 = str(j) + ".txt"
        fileNum4 = str(j%10+1)
        open("G:\\5kw\\" + fileNum4 + "\\" + fileName4, "w")
        print("G:\\5kw\\" + fileNum4 + "\\"  + fileName4)

threads = []
t1 = threading.Thread(target=fileWirtekw)
threads.append(t1)
t2 = threading.Thread(target=fileWirte2kw)
threads.append(t2)
t3 = threading.Thread(target=fileWirte3kw)
threads.append(t3)
t4 = threading.Thread(target=fileWirte4kw)
threads.append(t4)
if __name__ == '__main__':
    Time1 = time.time()
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    #print "all over %s" %ctime()
    Time2 = time.time()
    print("t="+str(Time2-Time1))
