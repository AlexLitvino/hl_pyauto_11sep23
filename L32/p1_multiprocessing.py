# About Windows

from multiprocessing import Process, Manager, Value
from time import sleep


# def do_job(n, message, wait, output):
#     i = 0
#     for i in range(n):
#         print(f"{message} {i}")
#         i = i + 1
#         sleep(wait)
#     output['result'] = i
#     return i
#
# if __name__ == '__main__':
#     output = {}
#     sleep(4)
#
#
#     process = Process(target=do_job, args=(10, 'In process', 0.5, output))
#     process.start()
#
#     for i in range(5):
#         print("In main")
#         sleep(0.4)
#
#     process.join()
#     print("Joined")
#     sleep(5)
#     print(output)

# ######################################################################################################################

# def do_job(n, message, wait, output):
#     i = 0
#     for i in range(n):
#         print(f"{message} {i}")
#         i = i + 1
#         sleep(wait)
#     output['result'] = i
#     return i
#
# output = Manager().dict()  # .array()
#
# process = Process(target=do_job, args=(10, 'In process', 0.2, output))
# process.start()
#
# for i in range(5):
#     print("In main")
#     sleep(0.4)
#
# process.join()
# print(output)

# ######################################################################################################################


def do_job(n, message, wait, output):
    i = 0
    for i in range(n):
        print(f"{message} {i}")
        i = i + 1
        sleep(wait)
    i = 128
    output.value = i
    return i


import ctypes
#output = Value('i')
output = Value(ctypes.c_byte)

process = Process(target=do_job, args=(10, 'In process', 0.2, output))
process.start()

for i in range(5):
    print("In main")
    sleep(0.4)

process.join()
print(output)
print(output.value)