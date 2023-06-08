from threading import Thread
import time

def do_func(value):
    # add work here, could be any of those IO bound tasks
    time.sleep(1) # simulate the long running task 
    print(f'Task {value} is done')

if __name__ == '__main__':
    start = time.perf_counter()
    # create threads
    threads = [Thread(target=do_func, args=(i,)) for i in range(20)]
    # start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print('All threads are executed successfully')   
    print(f'Total time taken  : {round(finish - start, 2)} seconds') 

