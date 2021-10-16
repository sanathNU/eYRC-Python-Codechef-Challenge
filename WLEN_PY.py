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
'''
Sample Input
2
@Debugging is being the detective in a criminal movie where you are also the murderer
@Good code is its own best documentation

Sample Output
9,2,5,3,9,2,1,8,5,5,3,3,4,3,8
4,4,2,3,3,4,13
'''
#list comprehension for storing all input strings as a list of words
ls =[list(map(str,input().split())) for i in range(int(input()))]
for items in ls:
    #removing the '@' from the beginning of each word of testcase
    items[0]=items[0][1:]
    #finding the length of each word and printing it
    a =[len(x) for x in items]
    print(','.join(map(str,a)))
