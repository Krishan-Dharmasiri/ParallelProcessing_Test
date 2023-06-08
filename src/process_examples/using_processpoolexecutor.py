import concurrent.futures
import time

def do_func(value: int)->int:
    '''
        Do work, this could be any of those CPU bound tasks
    '''    
    time.sleep(1) # Simulate the  long running task
    return value * value

def main():
    '''
        Using the context manager and  process pool executor
        A future is not the result but a promise to deliver the result in a later time
        you use the "result()" function to get the result froma future object
    '''
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(do_func, i) for i in range(20)]
        
        
    for future in concurrent.futures.as_completed(futures):
            print(f'Result :  {future.result()}')

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)') 