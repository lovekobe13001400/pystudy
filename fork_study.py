import os

'''
fork
'''
# print('process (%s) start...'%os.getpid())
#
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s'%(os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)'%(os.getpid(),pid))

from multiprocessing import  Process

#子进程要执行的代码(跨平台)
# def run_proc(name):
#     print('Run child process %s (%s)'%(name,os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s'%os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     p.start()
#     p.join()
#     print('Child process end')


#pool 启动大量的子进程，可以用进程池的方式批量创建子进程：
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print("Run task %s (%s)"%(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.'%(name,(end-start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.'%os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('waiting for all subpprocesses done')
#     p.close()
#     p.join()
#     print('All subprocess done')

###子进程
# import subprocess
# print('$  nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code',r)

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# #进程间的通信
# from multiprocessing import Process,Queue
# import os,time,random
# def write(q):
#     print('Process to write:%s'% os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s queue...'% value)
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('Process to read:%s'%os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue'%value)
#
# if __name__ == '__main__':
#     #父进程创建queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     #启动子进程pw，写入
#     pw.start()
#     #启动子进程pr,读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()

# import time,threading
# #新线程执行的代码
# def loop():
#     print('thread %s is running...'% threading.current_thread().name)
#     n = 0
#     while n<5:
#         n = n + 1
#         print('thread >>> %s'%(threading.current_thread().name))
#         time.sleep(1)
#     print('thread %s ended...'% threading.current_thread().name)
# print('thread %s is running...'% threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended'% threading.current_thread().name)


# import time,threading
# balance = 0
# #线程锁
# lock = threading.Lock()
# def change_id(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#
#     for i in range(1000000):
#         #当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码
#         lock.acquire()
#         try:
#             change_id(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# #结束再往下运行
# t1.join()
# t2.join()
# print(balance)

# import threading
# #创建全局ThreadLocal对象
# local_school = threading.local()
#
# def process_student():
#     std = local_school.student
#     print('Hello,%s(in %s)'%(std,threading.current_thread().name))
# #x线程函数
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
# t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


#分布式进程
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')