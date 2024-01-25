from threading import Thread
from time import sleep


def do_job1():
    for i in range(5):
        print(f"In do_job1 {i}")
        sleep(0.2)


def do_job2():
    for i in range(5):
        print(f"In do_job2 {i}")
        sleep(0.7)


thread1 = Thread(target=do_job1)
thread2 = Thread(target=do_job2)
thread1.start()
thread2.start()


for i in range(5):
    print(f"In main {i}")
    sleep(0.5)