import threading
import time
 
def task1():
    time.sleep(5)
    
 
def task2():
    print("hehreheh")
 

t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')

t1.start()
t2.start()

t1.join()
t2.join()