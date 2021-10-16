# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:15:50 2021

@author: FranticUser
"""

'''Created for CodeChef Problem SLICE1_PY
Problem Definition
Given a list L of numbers and its length, your task is to read these numbers into an array or a list.

Assuming the index starts from 0, use the slice operations to do the following operations:

print list in reverse order
for every third number starting with index 0, add 3 to it and print them
for every fifth number starting with index 0, subtract 7 from it and print
add all the numbers whose index is in between 3 and 7 (inclusive) and print the result
'''
'''
Sample Input
1
8
-2 3 -5 1 8 -4 2 7

Sample Output
7 2 -4 8 1 -5 3 -2
4 5
-11
14
'''
#number of testcases
nOfTest = int(input())
for i in range(nOfTest):
    #length of input list
    aLen = int(input())
    mainList = list(map(int,input().split()))
    #creating the required lists 
    revList = mainList[::-1]
    Index3 = [mainList[x]+3 for x in range(1,aLen) if x%3==0]
    Index5 = [mainList[x]-7 for x in range(1,aLen) if x%5==0]
    FinalSum = sum(mainList[3:8])
    
    #printing out the stuff
    print(' '.join(map(str,revList)))
    print(' '.join(map(str,Index3)))
    print(' '.join(map(str,Index5)))
    print(FinalSum)
    
