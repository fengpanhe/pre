# import os
import multiprocessing


def exec_test(a, b):
    print("exec" + str(a))


aa = []


class ClockProcess(multiprocessing.Process):

    def __init__(self, bb):
        multiprocessing.Process.__init__(self)
        self.bb = bb

    def run(self):
        aa.append(self.bb)
        print(aa)


if __name__ == '__main__':
    aa.append(-1)
    for i in range(4):
        p = ClockProcess(i)
        # p = multiprocessing.Process(target=exec_test, args=(i, 1))
        p.start()
    # for i in range(4):
    #     argcv = ['python3', 'test_exec.py', str(i)]
    #     pid = os.fork()
    #     if pid == 0:
    #         print(argcv)
    #         os.execvp('python3', argcv)
    #     print("a")
