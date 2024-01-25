from threading import Thread
from time import sleep


# def do_job(n, message, wait):
#     for i in range(n):
#         print(f"{message} {i}")
#         sleep(wait)
#
#
# thread1 = Thread(target=do_job, args=(5, "In do_job1", 0.8), daemon=True)
# thread1.start()
#
#
# for i in range(5):
#     print(f"In main {i}")
#     sleep(0.3)

# def do_job():
#     i = 0
#     while True:
#         i += 1
#         print(f"In job {i}")
#         sleep(0.8)
#
# thread1 = Thread(target=do_job, daemon=True)
# thread1.start()
#
# for i in range(5):
#     print(f"In main {i}")
#     sleep(0.3)

is_running = True
def do_job():
    i = 0
    while is_running:
        i += 1
        print(f"In job {i}")
        sleep(0.8)

thread1 = Thread(target=do_job)
thread1.start()

for i in range(5):
    print(f"In main {i}")
    sleep(0.3)
is_running = False


from queue import Queue
class Collector:

    def __init__(self):
        self.thread = Thread(target=self.collect)
        self.is_running = True
        self.thread.start()
        self.queue = Queue()

    def collect(self):
        self.queue.put(2)

    def stop_collector(self):
        self.is_running = False
