import time
import functools
import pandas as pd
import os

def time_spent(func):
    """This decorator prints the runtime of the decorated function
        and saves the runtime information in a csv with an "id" passed in via the "args" argument.
        
        Removing the "id" from the "lof_file" dataframe removes the dependency on an external input, 
        and the decorator can, thus, be used to log the runtime of any function.
    """
    @functools.wraps(func) 
    def wrapper_timer(*args, **kwargs):
        try:
            log_file = pd.read_csv(os.getcwd()+"\\log_file.csv")
        except:
            log_file = pd.DataFrame(columns=["id", "day_start", "time_start", "day_end", "time_end", "time_in_seconds", "func_name"])
        
        args_repr = [repr(a) for a in args]  
        
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] 
        
        start_time = time.perf_counter()   
        start_day = time.ctime()

        value = func(*args, **kwargs)
        
        end_time = time.perf_counter()     
        end_day = time.ctime()

        run_time = end_time - start_time   
        
        log_file = log_file.append({"id":args_repr[int(args_repr[0])], "day_start":start_day, "time_start":start_time, "day_end":end_day, "time_end":end_time, "time_in_seconds":run_time, "func_name":func.__name__}, ignore_index=True)
        
        log_file.to_csv(os.getcwd()+"\\log_file.csv", index=False)
        
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value 
    return wrapper_timer


#### Example Usage ####

# @time_spent
# def get_sum_x_times(*args, **kwargs):
#     for _ in range(args[args[0]]):
#         ff = sum([i**2 for i in range(10000)])
#     return ff

#### Here, the having 3 as the first argument means it will use 1000 as my range
# fg = get_sum_x_times(3, 400, 500, 1000, x = 200, y = 300)