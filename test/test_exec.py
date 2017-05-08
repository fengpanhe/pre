import sys

def exec_test(a):
    print("exec" + str(a))


if __name__ == '__main__':
   pid = sys.argv[1]
   exec_test(pid)