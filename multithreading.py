import threading
import time

def waking_up():
    time.sleep(8)
    print("i just woke up")

def brushing():
    time.sleep(4)
    print('brushing is done')

def shower():
    time.sleep(6)
    print('completed shower')


task1 = threading.Thread(target=waking_up)

task2 = threading.Thread(target=brushing)

task3 = threading.Thread(target=shower)



task1.start()
task2.start()
task3.start()

task1.join()
task2.join()
task3.join()

print('all tasks are completed')



