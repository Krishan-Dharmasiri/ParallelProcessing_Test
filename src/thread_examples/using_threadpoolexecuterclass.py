import concurrent.futures
import time

def do_func(value: int)->int:
    '''
        Do work, this could be any of those IO bound tasks
    '''    
    time.sleep(1) # Simulate the  long running task
    return value * value


def main():
    '''
        Using the context manager to manage the threads and  
        using "submit" function to call the long runnnig tasks
        Main difference here relative to the thread pool class is that this returns "futures"
        A future is not the result but a promise to deliver the result in a later time
        you use the "result()" function to get the result froma future object
    '''
    with concurrent.futures.ThreadPoolExecutor() as exe:
        futures = [exe.submit(do_func, i) for i in range(20)]
        
        
    # handle results as tasks are completed
    for future in concurrent.futures.as_completed(futures):
        print(f'Completed Futures : {future.result()}')   


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)')    