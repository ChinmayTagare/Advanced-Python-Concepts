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
import concurrent.futures

start = time.perf_counter()

def do_something(sec):
    print('Sleeping for {} seconds ... '.format(sec))
    time.sleep(sec)
    return 'Done sleeping for... {}'.format(sec)


# submit method schedules a function to be executed
# and returns a future object
# future object encapsulates the execution of function and allows
# us to check in on it after it schedules - we can check if it is running or its done
# also we can check the results
# if we grab the results, it will give the return value of the function
# added return in do_something

with concurrent.futures.ThreadPoolExecutor() as executor:
# =============================================================================
#     secs = [5,4,3,2,1]
#     results = [executor.submit(do_something, sec) for sec in secs]

#     # printing completed results
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#     
# =============================================================================
    # map returns the results, not future object like submit method
    secs = [5,4,3,2,1]
    # also, map will return the result as they started, not as completed
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)
    

# =============================================================================
# thread_list = []
# 
# for _ in range(10):
#     t = threading.Thread(target = do_something, args = [1.5])
#     t.start()
#     thread_list.append(t)
# 
# for thread in thread_list:
#     thread.join()
# 
# =============================================================================

finish = time.perf_counter()

print('Finished in {} seconds.'.format(round(finish-start, 2)))




























