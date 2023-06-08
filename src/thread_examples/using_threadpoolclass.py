from multiprocessing.pool import ThreadPool
import time

def do_func(value:int)->int:
    '''
        Do work, this could be any of those IO bound tasks
    '''    
    time.sleep(1) # Simulate the  long running task
    return value * value


def main():
    '''
        by default it uses threads that are equal to the number of logical CPUs available in the system
        you can fix the number of threads using "processes" argument here
        ThreadPool(processes = 20) => 20 threads created in the pool
    '''
    
    # when you use the "with" command, the pool will be automatically closed once that tasks are completed.
    with ThreadPool() as pool:
        results = pool.map(do_func, range(20))

        for result in results:
            print(f'Result : {result}')

    print('Done')

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)')
    