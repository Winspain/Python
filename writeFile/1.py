#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print i
        #sleep(1)

def move(func):
    for i in range(2):
        print i
        #sleep(4)

threads = []
t1 = threading.Thread(target=music)
threads.append(t1)
t2 = threading.Thread(target=move)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print "all over %s" %ctime()
