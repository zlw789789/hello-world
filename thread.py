#!/usr/bin/python3

import threading
import time

class mythread(threading.Thread):
    """docstring for mythread"""

    def __init__(self):
        super(mythread, self).__init__()

    def run(self):
        global num
        time.sleep(1)
        mutex.acquire()
        print(mutex.acquire())
        if mutex.acquire():
            num += 1
            print('this is the %s,the num is %s' % (self.name, num))
            mutex.release()

num = 0
mutex=threading.RLock()

def funa():
    for x in range(0, 10):
        th1 = mythread()
        th1.start()

# for x in range(0,100):
# 	th1=mythread()
# 	th1.start()

if __name__ == '__main__':
    funa()
    print(num)
