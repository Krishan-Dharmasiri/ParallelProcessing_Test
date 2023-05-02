import multiprocessing

def print_func(continent='Asia'):
    print(f'The name of continent is : {continent}')

if __name__ == '__main__':
    names = ['America', 'Europe', 'Africa']
    processes = []
    for name in names:
        proc = multiprocessing.Process(target=print_func, args=[name]) 
        processes.append(proc)
        proc.start()  

    for proc in processes:
        proc.join()    