import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import os
import time
import threading
import random

p_exec = ThreadPoolExecutor(max_workers=3)

def method(arg=None):
        tid = threading.current_thread()
        #print "starting method {}".format(tid)
        sl_time = random.randrange(2,11)
        print("\n   >> {} executing task for {}.........".format(tid, sl_time))
        time.sleep(sl_time)
        print("                 >> {} task execution completed!".format(tid))


#for i in range(10):
if __name__ == "__main__":
        for i in range(10):
                ret1 = p_exec.submit(method)
