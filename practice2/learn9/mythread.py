# 多线程
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


'''
threading模块有个current_thread()函数，它永远返回当前线程的实例
进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
主线程实例的名字叫MainThread，
子线程的名字在创建时指定，我们用LoopThread命名子线程
'''