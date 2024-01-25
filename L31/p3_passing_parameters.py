from threading import Thread
from time import sleep


def do_job(n, message, wait):
    for i in range(n):
        print(f"{message} {i}")
        sleep(wait)


thread1 = Thread(target=do_job, args=(5, "In do_job1", 0.2))
thread2 = Thread(target=do_job, kwargs={"n": 5, "message": "In do_job2", "wait": 0.7})
thread1.start()
thread2.start()

for i in range(5):
    print(f"In main {i}")
    sleep(0.5)
