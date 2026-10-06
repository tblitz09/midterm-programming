import time
import random

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
    
    size = [100, 1000, 5000, 10000, 50000, 100000]

    for n in size:
        slow_times = []
        fast_times = []
        data = [random.randint(0, 100000) for _ in range(n)]

        for j in range (0, 10):
            start_time = time.perf_counter()
            find_duplicates_slow(data)
            end_time = time.perf_counter()
            slow_times.append(end_time - start_time)
    
            start_time_2 = time.perf_counter()
            find_duplicates_fast(data)
            end_time_2 = time.perf_counter()
            fast_times.append(end_time_2 - start_time_2)
        fast_average = sum(fast_times) / 10
        slow_average = sum(slow_times) / 10
        print(f"for n = {n} (n = size)")
        print(f"Fast alg average time = {fast_average} seconds")
        print(f"Slow alg average time = {slow_average} seconds")
        print()


if __name__ == "__main__":
    flawed_benchmark()