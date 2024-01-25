from threading import Thread
from time import sleep


def do_job():
    i = 0
    message = "In job"
    for i in range(10):
        print(f"{message} {i}")
        i = i + 1
        sleep(0.2)
    return i


class CustomThread(Thread):

    def __init__(self, target, id_=0):
        super().__init__(target=target)
        self.id = id_
        self.result = None

    def run(self) -> None:
        self.result = self._target()

    def join(self, timeout=None) -> None:
        super().join(timeout)
        return self.result


thread = CustomThread(do_job)
thread.start()
print(thread.result)
sleep(0.5)
print(thread.result)
result = thread.join()
print(result)


#thread1 = Thread(target=do_job, args=(5, "In do job ", 0.2, output))
#thread1.start()
#thread1.join()