# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:52:37 2021

@author: FranticUser
"""

''' Created for solving the CodeChef Problem STAR_PY
Problem Statement:
    Given a number N, generate a star pattern such that on the first line there are N stars and on the subsequent lines the number of stars decreases by 1.

    The pattern generated should have N rows. In every row, every fifth star (*) is replaced with a hash (#).

     row should have the required number of stars (*) and hash (#) symbols.
'''
'''
Sample Input
1
5
Sample Output
****#
****
***
**
*
'''
#list comprehension for taking all inputs
ls = [int(input()) for i in range(int(input()))]
for items in ls:
    #creating individual strings with '*' and then replacing every 5th element with '#'
    temp = items * '*'
    temp1=[]
    for a in range(1,items+1):
        if a%5==0 and a!=0:
            temp1.append('#')
        else:
            temp1.append('*')
    #printing each temp string          
    for b in range(items):
        print(''.join(temp1))
        temp1=temp1[:-1]                                                              
