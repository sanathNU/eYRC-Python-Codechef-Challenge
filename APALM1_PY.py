# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:12:52 2021

@author: FranticUser
"""

'''Created for solving APALM1_PY in CodeChef
Problem Definition:
    This task is to generate Arithmetic Progression (A.P.) and perform few operations on the series. The first term of sequence a1, the common difference between terms d and the number of terms n in series is given.

    You have to generate the A.P. series in a given function. The code stub provided here is to be used. It calls the function generate_AP() to generate the A.P. series and return it.

    Then with the use of lambda and map functions, find squares of the terms in series and print it. Finally with the use of reduce function, compute the sum of the squares of terms in series and print it.
'''
'''
Sample Input
1
2 5 7

Sample Output
2 7 12 17 22 27 32
4 49 144 289 484 729 1024
2723
'''
#code stub given by codechef
'''
This script is code stub for CodeChef problem code APLAM1_PY
Filename:      APLAM1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''
# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):
    ap_form = lambda a,d,n: [a+d*(x-1) for x in range(1,n+1)]
    AP_series = ap_form(a1,d,n)
    # Complete this function to return A.P. series
    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the a1, d and n values
    for _ in range(test_cases):
        a1,d,n = map(int,input().split())
        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)

        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = list(map(lambda x:x*x,AP_series))

        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce(lambda a, b: a+b, sqr_AP_series)
        #Printing all the outputs       
        print(' '.join(map(str,AP_series)))
        print(' '.join(map(str,sqr_AP_series)))
        print(sum_sqr_AP_series)
