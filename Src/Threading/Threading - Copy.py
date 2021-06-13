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
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping for 1 second ... ')
    time.sleep(1)
    print('Done sleeping... ')

t1 = threading.Thread(target = do_something)
t2 = threading.Thread(target = do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print('Finished in {} seconds.'.format(round(finish-start, 2)))




























