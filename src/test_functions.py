import numpy as np
from math import sqrt

def square_root(val, tol=1e-4):
    """ This is a docstring. Here I would explain what the square_root() function does. (It calculates the square root. Duh.)

    :param a: The value whose square root you want to calculate.
    :type a: float
    :param tol: The tolerance of the solver. Smaller tolerance leads to higher precision. Default: 1e-4.
    :type tol: float

    :returns: The square root of parameter *val*
    :rtype: float

    :Example:

      >>> value = square_root(4)
      >>> print(value)
      2.0
    """
    # Define the initial guess and initialize the new guess and counter variables
    guess = val*0.5
    guess_new = 0.01
    counter = 0

    # Execute "Newton's" algorithm for calculating the square root
    while ((guess-guess_new)/guess_new > tol):
        # Update the guess to the new value as the loop proceeds
        if (counter>0):
            guess = guess_new
        guess_new = 0.5*(guess + val/guess)
        counter = counter + 1
    return guess_new

def mean_val(a, b):
    """
    This function returns the mean of arguments a and b: 0.5(a + b)

    :param a: The first value.
    :type a: float
    :param b: The second value.
    :type b: float

    :returns: The mean value.
    :rtype: float

    :Example:

        >>> mean_val(2, 5)
        3.5
    """
    return 0.5*(a + b)

mean_val(2,5)
