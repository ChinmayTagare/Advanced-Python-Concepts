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
import concurrent.futures

start = time.perf_counter()

def do_something(secs):
    print('Sleeping for {} seconds ... '.format(secs))
    time.sleep(secs)
    return 'Done sleeping... '

# lot less code using pool executor and list comperhension
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]
        
        # using as completed iterator
        for f in concurrent.futures.as_completed(results):
            print(f.result())
# =============================================================================
#     f_obj1 = executor.submit(do_something, 1)
#         f_obj2 = executor.submit(do_something, 1)
#         print(f_obj1.result())
#         print(f_obj2.result())
# =============================================================================
    # =============================================================================
    # process_list = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     process_list.append(p)
    #     
    # for process in process_list:
    #     process.join()
    # 
    # =============================================================================
    
finish = time.perf_counter()
    
print('Finished in {} seconds.'.format(round(finish-start, 2)))




























