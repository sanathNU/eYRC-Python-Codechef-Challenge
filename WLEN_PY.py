# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:38:02 2021

@author: FranticUser
"""

''' Created for solving CodeChef Problem WLEN_PY
Problem Definition:
    Write a program to read a string str, which will contain words separated with space.

    Your task is to count the length of each word and print it. The output should be comma-separated string.

    Each string str will begin with "@".
'''
ls =[list(map(str,input().split())) for i in range(int(input()))]
for items in ls:
    items[0]=items[0][1:]
    a =[len(x) for x in items]
    print(','.join(map(str,a)))