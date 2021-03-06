"""
Topic  : Threading in Python
Author : Chinmay Tagare
"""

# Threading is used for IO bound tasks
# where function takes inputs and waits for another input to get in
# IO bound taks includes - file processing, input/output variables etc
# where as, CPU bound tasks we need to use multiprocessing
# CPU bound tasks include data crunching, handling large data etc


import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second ... ')
    time.sleep(1)
    print('Done sleeping... ')

if __name__ == '__main__':
    process_1 = multiprocessing.Process(target=do_something)
    process_2 = multiprocessing.Process(target=do_something)
    
    process_1.start()
    process_2.start()
    
    process_1.join()
    process_2.join()
    
    finish = time.perf_counter()
    
    print('Finished in {} seconds.'.format(round(finish-start, 2)))




























