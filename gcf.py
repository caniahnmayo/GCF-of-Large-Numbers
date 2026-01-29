# CMSC 503: Computer Science and Engineering Fundamentals
# Lab 9: Sum of i^3 for i=1 to i=n
# Professor: Dr. Lee
# File Created: 2026.01.07
# File Updated: 2026.01.07

import time
import tracemalloc

# sum_cubes_loop sums i^3 for i=1 to i=n using a for loop
def sum_cubes_loop(n):
    sum = 0
    for i in range(1, n + 1):                                # For i from 1 to n
        sum = sum + i**3                                     # Add the result of i^3 to the sum
    return sum
    
# sum_cubes_loop sums i^3 for i=1 to i=n using a formula
def sum_cubes_formula(n):
    return (n*((n+1)/2))**2                                  # Using the formula to find the sum of the cubes

def main():
    
    # For n = 1000 using loop method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using loop method: {sum_cubes_loop(1000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
    # For n = 1000 using formula method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using formula method: {sum_cubes_formula(1000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
    # For n = 100000 using loop method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using loop method: {sum_cubes_loop(100000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
    # For n = 100000 using formula method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using formula method: {sum_cubes_formula(100000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
    # For n = 1000000 using loop method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using loop method: {sum_cubes_loop(1000000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
    # For n = 1000000 using formula method
    tracemalloc.start()                                      # Starting the the memory trace to measure memory usage           
    start_time = time.perf_counter()                         # Starting the timer to measure time usage

    # Printing the results
    print(f"Summing i^3 for i=1 to i=n using formula method: {sum_cubes_formula(1000000)}")

    end_time = time.perf_counter()                           # Stopping the timer
    runtime = end_time - start_time                          # Calculating run time start_time - end_time
    peak_mem = tracemalloc.get_traced_memory()               # Getting memory trace, highest amount of memory used stored in peak_memory[1]
    tracemalloc.stop()                                       # Stopping the memory trace
    print(f"Run Time: {runtime}s")                           # Print run time in seconds
    print(f"Peak Memory: {peak_mem[1] / 1024:.2f} KB")       # Print memory usage in KB
    
main()