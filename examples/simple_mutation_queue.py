#!/usr/bin/env python

"""
A simple example of sequential computation using a function, attempting to
modify a list/array.
"""

import pprocess
import time
#import random

# Array size.

N = 10
limit = 10
delay = 1

# Work function.

def calculate(results, i, j):

    """
    A supposedly time-consuming calculation on 'results' using 'i' and 'j'.
    """

    #time.sleep(delay * random.random())
    time.sleep(delay)
    results[i * N + j] *= 2

# Main program.

if __name__ == "__main__":

    t = time.time()

    queue = pprocess.Queue(limit=limit)
    calc = queue.manage(pprocess.MakeParallel(calculate))

    # Initialise an array.

    results = list(range(0, 100))

    # Perform the work.

    print("Calculating...")
    for i in range(0, N):
        for j in range(0, N):
            calc(results, i, j)

    # Show the results.

    for i in range(0, N):
        for result in results[i*N:i*N+N]:
            print(result, end=' ')
        print()

    print("Time taken:", time.time() - t)

# vim: tabstop=4 expandtab shiftwidth=4
