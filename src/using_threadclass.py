from threading import Thread

def do_func(value):
    # add work here
    print(f'Task {value} is done')

if __name__ == '__main__':
    # create threads
    threads = [Thread(target=do_func, args=(i,)) for i in range(20)]
    # start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    print('All threads are executed successfully')    

