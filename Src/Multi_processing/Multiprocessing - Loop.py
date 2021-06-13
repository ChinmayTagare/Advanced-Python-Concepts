"""
Topic  : Threading in Python
Author : Chinmay Tagare
"""

# Threading is used for IO bound tasks
# where function takes inputs and waits for another input to get in
# IO bound taks includes - file processing, input/output variables etc
# where as, CPU bound tasks we need to use multiprocessing
# CPU bound tasks include data crunching, handling large data etc

# _ is throw away variable 

import time
import multiprocessing

start = time.perf_counter()

def do_something(secs):
    print('Sleeping for {} seconds ... '.format(secs))
    time.sleep(secs)
    print('Done sleeping... ')

if __name__ == '__main__':
    
    process_list = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        process_list.append(p)
        
    for process in process_list:
        process.join()
    
    
    finish = time.perf_counter()
    
    print('Finished in {} seconds.'.format(round(finish-start, 2)))




























