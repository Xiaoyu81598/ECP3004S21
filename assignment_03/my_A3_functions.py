# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules



##################################################

# import name_of_module




##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def quad_roots_1(x: float, a: float, b: float, c: float) -> float:

    """Return two real-valued roots of the quadratic equation.

 

    >>> quad_roots_1(3,1,7,12)

    [-3.0, -4.0]

    >>> quad_roots_1(-5,1,2,-35)

    [5.0, -7.0]

    >>> quad_roots_1(1.5,1,-5.5,6)

    [4.0, 1.5]

    """

    d = (b**2) - (4*a*c)

    x_1 = (-b+math.sqrt(d))/(2*a)

    x_2 = (-b-math.sqrt(d))/(2*a)

 

    return [x_1,x_2]



# Define the rest of your functions for Exercises 2-4.
 

# Exercise 2


# Exercise 3


# Exercise 4



# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating name_of_function(0, 0)")
print("Expected: " + str(answer_you_expect))
print("Got: " + str(name_of_function(0, 0)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
# ...


print("#" + 50*"-")
print("Exercise 1, Example 3:")
# ...


# ...

# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")


# ...


##################################################
# End
##################################################