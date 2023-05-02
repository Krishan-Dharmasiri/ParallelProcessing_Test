import concurrent.futures

def do_func(value:int)->int:
    return value

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(do_func, i) for i in range(50)]
        for future in concurrent.futures.as_completed(futures):
            print(f'>got {future.result}')
        # issue one task for each call to the function
        for result in executor.map(do_func, range(50)):
            print(f'>got {result}')


if __name__ == '__main__':
    main()