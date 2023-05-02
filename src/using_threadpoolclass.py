from multiprocessing.pool import ThreadPool
import time

def do_func(value:int)->int:
    time.sleep(1)
    return value * value


def main():
    with ThreadPool() as pool:
        results = pool.map(do_func, range(10))

        for result in results:
            print(f'Result : {result}')

    print('Done')

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    finish = time.perf_counter()
    print(f'Time Taken : {round(finish - start, 2)} second(s)')
    