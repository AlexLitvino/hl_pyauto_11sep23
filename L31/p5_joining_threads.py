from threading import Thread
from time import sleep


def do_job(n, message, wait):
    for i in range(n):
        print(f"{message} {i}")
        sleep(wait)


thread1 = Thread(target=do_job, args=(5, "In do_job1", 0.2))
thread1.start()

# for i in range(5):
#     print(f"In main1 {i}")
#     sleep(0.1)

thread1.join(timeout=0.3)

for i in range(5):
    print(f"In main2 {i}")
    sleep(0.5)