from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

# 创建子进程时，只需要传入一个执行函数和函数的参数，
# 创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


# 进程池
'''
对Pool对象调用join()方法会等待所有子进程执行完毕，
调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了。
ask 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程
p = Pool(5)默认大小是CPU的核数，如果你不幸拥有8核CPU，
你要提交至少9个子进程才能看到上面的等待效果
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


