import concurrent.futures

def do_func(value: int)->int:
    return value


def main():
    with concurrent.futures.ThreadPoolExecutor() as exe:
        futures = [exe.submit(do_func, i) for i in range(50)]
        # handle results as tasks are completed
        

    for future in concurrent.futures.as_completed(futures):
        print(f'Completed Futures : {future.result()}')   


if __name__ == '__main__':
    main()    