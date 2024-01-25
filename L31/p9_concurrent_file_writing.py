from threading import Thread
from time import sleep

def writer(file, data):
    for i in range(100):
        with open(file, 'a') as f:
            f.write(data + '\n')

# thread1 = Thread(target=writer, args=('output.txt', '1111************************************************************'))
# thread2 = Thread(target=writer, args=('output.txt', '2222====='))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


# data = ['1111************************************************************', '2222=====']
# threads = []
# for line in data:
#     thread = Thread(target=writer, args=('output.txt', line))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()

data = ['1111************************************************************', '2222=====']
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for line in data:
        futures.append(executor.submit(writer, "output.txt", line))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
