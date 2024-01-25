from threading import Thread
from time import sleep


def do_job(n, message, wait, output):
    i = 0
    for i in range(n):
        print(f"{message} {i}")
        i = i + 1
        sleep(wait)
    output['result'] = i
    return i


output = {}
thread1 = Thread(target=do_job, args=(5, "In do job ", 0.2, output))
thread1.start()
thread1.join()
print(output)

for i in range(5):
    print(f"In main2 {i}")
    sleep(0.5)

print(output['result'])
