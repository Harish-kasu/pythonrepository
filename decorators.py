def log_execution(fun):
    def wrapper(*args,**kwargs):
        print("functiond started")
        fun()
        print("function completed")
    return wrapper
    
@log_execution
def  base_function():
     print("hello world ")




base_function()




    