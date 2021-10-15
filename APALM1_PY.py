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
ls=[tuple(map(int,input().split())) for i in range(int(input()))]
ap_form = lambda a,d,n: [a+d*(x-1) for x in range(1,n+1)]

for items in ls:
    a,d,n = items
    series = ap_form(a,d,n)
    sq_series = list(map(lambda x:x*x,series))
    sq_sum = sum(sq_series)
    print(' '.join(map(str,series)))
    print(' '.join(map(str,sq_series)))
    print(sq_sum)