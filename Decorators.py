import time


def check_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()

        print("start time ", t2, "end time", t1)

    return wrapper()


@check_time
def f1():
    print("inside f1")
    for i in range(5):
        pass


@check_time
def f2():
    print("inside f2")
    for i in range(10):
        pass


def non_decorated_fun():
    print("inside non decorated func")


if __name__ == "__main__":
    print("here")
    non_decorated_fun()
