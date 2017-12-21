# A simple function to approximate the square root of positive real numbers

import math
import random

# Takes a real number and approximates its square root within tolerance
def square_root(a, tolerance = 0.00001, max_iterations = 100):
    if a < 0: # This is illegal input
        return -1
    if a == 1: # This is a unique edge case
        return 1
    if a == 0: # This is a unique edge case
        return 0

    # Start with initial estimate and iteratively improve it
    estimate = 1
    iteration = 0
    while abs(estimate ** 2 - a) > tolerance and iteration < max_iterations:
        step_value = (abs(estimate ** 2 - a) * .05) % 100

        if estimate ** 2 < a:
            estimate += step_value
        else:
            estimate -= step_value
        iteration += 1

    return estimate

if __name__ == '__main__':
    # These square roots are well known, so test them
    common_roots = [0.25, 0.5, 0.99, 0, 1, 2, 4, 5, 9, 16, 25, 36, 81, 100, 144, 1000, 125000]

    # Build list of random roots
    small = [random.random() for i in range(100)]
    medium = [random.random() + 100 for i in range(100)]
    large = [random.random() + 10000 for i in range(100)]

    # Combine all lists into one list of test values
    test = [common_roots, small, medium, large]
    sizes = ["common roots", "small", "medium", "large"]

    # Test performance on all values
    tol = 0.00001
    print "Testing on %s numbers with tolerance of %s" % (len(test), tol)
    for i in range(len(test)):
        num_wrong = 0
        for num in test[i]:
            if abs(square_root(num, tolerance = tol) - math.sqrt(num)) >  tol:
                num_wrong += 1
        print "Square Root approximation got %s%% wrong with size %s." % ((num_wrong * 1.0 / len(test[i])) * 100, sizes[i])
