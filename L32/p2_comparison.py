from time import sleep, perf_counter_ns
from threading import Thread
from multiprocessing import Process

NS = 1000_000_000


def do_io_job(n):
    for i in range(n):
        print("Start waiting")
        sleep(1)
        print("End waiting")


def do_cpu_job(n):
    import random
    import math
    for _ in range(n):
        lst = [random.random() for i in range(1000_000)]
        [math.sin(i) for i in lst]
        [pow(i, 4.454355) for i in lst]


if __name__ == '__main__':
    # 4 external, 4 internal iterations

    # start_time1 = perf_counter_ns()
    # for i in range(4):
    #     do_io_job(4)
    # end_time1 = perf_counter_ns()
    # sync_io = (end_time1 - start_time1) / NS
    #
    # threads = []
    # for i in range(4):
    #     thread = Thread(target=do_io_job, args=(4,))
    #     threads.append(thread)
    # start_time2 = perf_counter_ns()
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # end_time2 = perf_counter_ns()
    # async_io = (end_time2 - start_time2) / NS
    #
    # processes = []
    # for i in range(4):
    #     process = Process(target=do_io_job, args=(4,))
    #     processes.append(process)
    # start_time3 = perf_counter_ns()
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()
    # end_time3 = perf_counter_ns()
    # parallel_io = (end_time3 - start_time3) / NS
    #
    # print(f"Sync: {sync_io}")
    # print(f"Async: {async_io}")
    # print(f"Parallel: {parallel_io}")
    # # async > sync > parallel


    start_time1 = perf_counter_ns()
    for i in range(4):
        do_cpu_job(4)
    end_time1 = perf_counter_ns()
    sync_cpu = (end_time1 - start_time1) / NS

    threads = []
    for i in range(4):
        thread = Thread(target=do_cpu_job, args=(4,))
        threads.append(thread)
    start_time2 = perf_counter_ns()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time2 = perf_counter_ns()
    async_cpu = (end_time2 - start_time2) / NS

    processes = []
    for i in range(4):
        process = Process(target=do_cpu_job, args=(4,))
        processes.append(process)
    start_time3 = perf_counter_ns()
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end_time3 = perf_counter_ns()
    parallel_cpu = (end_time3 - start_time3) / NS

    print(f"Sync: {sync_cpu}")
    print(f"Async: {async_cpu}")
    print(f"Parallel: {parallel_cpu}")
    # sync > parallel > async