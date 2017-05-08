# import os
import multiprocessing

manager = multiprocessing.Manager()
aa = []
aa = manager.list()


def exec_test(a, b):
    aa.append(a)
    print(str(aa))




class ClockProcess(multiprocessing.Process):

    def __init__(self, bb):
        multiprocessing.Process.__init__(self)
        self.bb = bb
        aa.append(self.bb)

    def run(self):
        print(str(aa))


if __name__ == '__main__':
    aa.append(-1)
    p = multiprocessing.Pool()
    for i in range(4):
        p.apply_async(exec_test, args=(i, 1))

        # p = ClockProcess(i)
        # p = multiprocessing.Process(target=exec_test, args=(i, 1))
        # p.start()
    # for i in range(4):
    #     argcv = ['python3', 'test_exec.py', str(i)]
    #     pid = os.fork()
    #     if pid == 0:
    #         print(argcv)
    #         os.execvp('python3', argcv)
    #     print("a")
    p.close()
    p.join()
