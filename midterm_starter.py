import time
import random
import matplotlib.pyplot as plt

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    This benchmarking function contains several methodological errors.
    Rewrite this function to properly and fairly compare the two algorithms to demonstrate their scaling behavior.
    """
    print("Running flawed benchmark...")
    
    size = [100, 1000, 2500, 5000, 7500, 10000] # Creates input sizes that will be used to test speed at different sizes
    slow_list = []
    fast_list = [] # Creates lists to take all the average times

    for n in size:
        slow_times = []
        fast_times = []
        data = list(range(n)) # Creates data that is a list of numbers from 1 to n

        for j in range (0, 10): # Tests each algorithm 10 times per size
            start_time = time.perf_counter()
            find_duplicates_slow(data)
            end_time = time.perf_counter()
            slow_times.append(end_time - start_time)
    
            start_time_2 = time.perf_counter()
            find_duplicates_fast(data)
            end_time_2 = time.perf_counter()
            fast_times.append(end_time_2 - start_time_2)
        fast_average = sum(fast_times) / 10
        slow_average = sum(slow_times) / 10 # Creates an average of the 10 times to see the average of the algorithms per size
        slow_list.append(slow_average)
        fast_list.append(fast_average) # Puts these average times into a list to be graphed
        print(f"for n = {n} (n = size)")
        print(f"Fast alg average time = {fast_average} seconds")
        print(f"Slow alg average time = {slow_average} seconds")
        print()

    # Plot Code
    plt.plot(size, fast_list, label="fast average time", color="red", marker="o")
    plt.plot(size, slow_list, label="slow average time", color="blue", marker="s")
    plt.title("Comparing fast vs slow algorithms with different size lists")
    plt.xlabel("size of list (n)")
    plt.ylabel("average time (seconds)")
    plt.legend()
    plt.grid((True))
    plt.savefig('results.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    flawed_benchmark()