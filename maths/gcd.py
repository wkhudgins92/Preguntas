# Input: List of integers
# Output: Greatest common divisor of all the integers (ie the largest number that divides each integer)
# Assumed all input will actually be numbers, so no need to worry about NaNs, nulls, empty, etc
# Runs in O(nk) time where n is the number of integers given to this function and k is a term to account for the fact that
# we have an inter loop that sometimes runs from the current gcd to 0.

def find_gcd(numbers):
    gcd = numbers[0]

    for i in range(0, len(numbers)):
        if numbers[i] % gcd == 0:
            continue
        for prospective_gcd in range(gcd - 1, 0, -1):
            if numbers[i] % prospective_gcd == 0 and gcd % prospective_gcd == 0:
                gcd = prospective_gcd
                break
    return gcd

if __name__ == '__main__':
    # Test cases for GCD, partially taken from: http://cs.au.dk/~chili/PBI04/ExamplePrograms/gcd_function_test.py
    testcases = [ (13, 13),              # trick case: a = b
                  (37, 600),              # first argument is a prime
                  (20, 100, 400, 2000),      # one is multiplum of other
                  (624129, 2061517) ] # straight case
    solutions = [13, 1, 20, 18913]

    for i in range(len(testcases)):
        print "Testing algorithm on:"
        print testcases[i]
        print "Calculated GCD is %s and it should be %s" % (find_gcd(testcases[i]), solutions[i])
        print " "
