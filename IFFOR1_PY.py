# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:51:58 2021

@author: FranticUser
"""

''' Created for CodeChef Problem IFFOR1_PY
Problem Statement:
    The task is to read an integer n from STDIN.

    For all values of i<n in ascending order, do the following:

        If i is non-zero then,

    print the square of i, if i is odd.
    print double the value of i, if i is even.
    If i is zero then, add 3 to i.
'''
nums = [int(input()) for i in range(int(input()))]
for stuff in nums:
    ls = []
    for i in range(stuff):
        if i==0:
            ls.append(3)
        elif i%2 !=0:
            ls.append(i*i)
        else:
            ls.append(2*i)
    
    print(' '.join(map(str,ls)))
    print('\n')