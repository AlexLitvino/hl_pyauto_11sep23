from threading import Thread, Lock, RLock, Timer
import time

#lock.acquire()
#method1()

#method2()
#lock.release()


class Employee:

    def __init__(self):
        self.salary = 0
        self.lock = RLock()

    def increase_salary(self):
        #with self.lock:
        #self.lock.acquire(timeout=2)
        self.lock.acquire()
        self.lock.acquire()
        local_var = self.salary
        local_var += 100
        time.sleep(1)
        self.salary = local_var
        self.lock.release()
        self.lock.release()


employee = Employee()

thread1 = Thread(target=employee.increase_salary)
thread2 = Thread(target=employee.increase_salary)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(employee.salary)
