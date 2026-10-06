# CMPSC 202 - Midterm Programming Assignment

Name: Tyler Biss

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

    1. Only one input size of the list is tested (n = 1000). Now different input sizes are made into a list and testing different input sizes with the algorithms. 
    2. The timing starts before the data thats tested is created, not truly testing the algorithms time. Data creation is done outside of the timing part of the algorithm. 
    3. The two algoritms were given different data to test. To effectively compare the two algorithms, the same dataset should be used. I fixed this by creating one dataset that is used for both algorithms.
    4. The data set could contain duplicates. This would cause the algorithm to finish early instead of fully moving through the data set. I changed this by making the data set a list of numbers from 1 to the input size. This allows the two algorithms to fully go through the data set. 
    5. The original only ran the algrothim once and used that time. I fixed this issue by having it run 10 times per algorithm and take the average of the 10. 
    6. The original used time.time() which is less effective than time.perfcounter() in algorithm running time comparisons. This is due to time.time() using the computer's internal clock to compare while perfcounter does not. So i replaced time.time() with time.perfcounter().

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.



