import multiprocessing
import time

def do_func(value: int)->int:
    '''
        Do work, this could be any of those CPU bound tasks
        E.g. Financial Modeling, Processing large datasets
    '''    
    time.sleep(1) # Simulate the  long running task
    print(f'Task {value} is done')

if __name__ == '__main__':
    start = time.perf_counter()

    processes = [multiprocessing.Process(target=do_func, args=(i,)) for i in range(20)]

    # Start all the process available in the list
    for process in processes:
        process.start()
    
    # Wait for all the processes to finish
    for proc in processes:
        proc.join()   
        

    finish = time.perf_counter()
    print(f'Total time taken  : {round(finish - start, 2)} seconds')     