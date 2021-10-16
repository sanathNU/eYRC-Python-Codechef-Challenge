# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:39:17 2021

@author: FranticUser
"""

''' Created for code chef problem PAL_PY
Problem STatement:
    Given a string str, check if its a palindrome. Consider it to be case insensitive.

    A palindrome string is a sequence of characters that reads the same forwards and backwards.

    If str is found to be a palindrome, print It is a palindrome
'''
'''
Sample Input
3
AhheioIehHA
OeaiensneIaIeO
wieowppwoeiw

Sample Output
It is a palindrome
It is not a palindrome
It is a palindrome
'''
# This list stores all test case inputs in uppercase, so as to satisfy the 'case insensitivity' criteria. 
main_ls=[str(input().upper()) for i in range(int(input()))]

for items in main_ls:
    # reversing the string and checking if they are the same
    if items==items[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
