'''
Import the Thread class from threading module
'''
from threading import Thread

def main() -> None:
    '''
        Function to run the thread
        Thread class takes 2 arguments, 
            "target" => the function to be executed by the new thread
            "args"   => argument to be passed into the "target" function
    '''
    # Create the new thread and assign the target function and the arguments at the same time
    thread_1 = Thread(target=print_cube, args=(10,))

    # start the thread
    thread_1.start()

    # wait until the thread is completely executed
    thread_1.join()

    # print a message to the caller once the program finishes
    print('thread executed successfully')


def print_cube(num : int) -> int:
    '''
    returns the cube of a given integer value
    '''    
    print('Cube : {}'.format(num * num * num))


if __name__ == '__main__':
    main()