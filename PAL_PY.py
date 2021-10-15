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
main_ls=[str(input().upper()) for i in range(int(input()))]

for items in main_ls:
    if items==items[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")