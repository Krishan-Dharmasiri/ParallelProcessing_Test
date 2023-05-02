from multiprocessing import Lock, Process, Queue, current_process
import time
import queue


def do_job(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()

        except queue.Empty:
            break

        else:
            print(task)
            tasks_that_are_done.put(task + ' is done by ' + current_process().name)
            time.sleep(.5)    

    return True    


def main():
    number_of_tasks = 10
    number_of_processes = 4
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    start = time.perf_counter()

    for i in range(number_of_tasks):
        tasks_to_accomplish.put('Task no ' + str(i))

    # Creating processes
    for w in range(number_of_processes):    
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()

    # completing process
    for p in processes:
        p.join()    

    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    finish = time.perf_counter()
    print(f'Time taken : {round(finish - start, 2)} second(s)')    

    return True 

if __name__ == '__main__':
    main()   