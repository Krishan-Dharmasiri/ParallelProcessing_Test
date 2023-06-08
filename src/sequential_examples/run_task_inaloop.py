import time

def do_func(value):
    # add work here, could be any of those IO bound tasks
    time.sleep(1) # simulate the long running task 
    print(f'Task {value} is done')


if __name__ == '__main__':
    start = time.perf_counter()

    for i in range(20):
        do_func(i)


    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 