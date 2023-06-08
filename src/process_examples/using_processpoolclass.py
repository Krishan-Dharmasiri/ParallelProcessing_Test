import multiprocessing
import time

def do_func(value:int)->int:
    '''
        Do work, this could be any of those CPU bound tasks
    '''    
    time.sleep(1) # Simulate the  long running task
    return value * value


def main()-> None:
    '''
        Using the Procee Pool class
        we can use "processes" paramater to specify how many process we need to create
        By default this creates number of processes equal to the logical CPUs available in the system
    '''
    with multiprocessing.Pool() as pool:
        results = pool.map(do_func, range(20))

    for result in results:
        print(f'Result : {result}')

    print('Done')


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)')
