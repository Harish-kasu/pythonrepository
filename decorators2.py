import time  

def time_it(func):
    def wrapper(*args,**kwargs):
        start_time =  time.time()
        print(f"start time is {start_time}")
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"end time is {end_time}")
        print(f"total time taken is {end_time - start_time = } seconds",result)
        return result
    return wrapper


@time_it
def slow_function():
    print("Running slow function...")
    time.sleep(2)
    print("Done!")


slow_function()




