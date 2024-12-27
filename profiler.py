import time
import os
import psutil

 
def elapsed_since(start):
    return time.perf_counter()-start
 
 
def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss
 
 
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        print(f"Calling {func.__name__}: Memory used {mem_after-mem_before} kB; Execution Time: {elapsed_time} s")
        return result
    return wrapper


if __name__=="__main__":
    @profile
    def foo(n: int):
        result = [x**2 for x in range(n)]
        return result
    
    print(foo(20))