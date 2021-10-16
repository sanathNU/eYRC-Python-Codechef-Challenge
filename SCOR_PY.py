# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:46:48 2021

@author: FranticUser
"""

'''Created for CodeChef Problem SCOR_PY
Problem Definition:
    There are N students in the class with distinct names. You are given a list of students and their scores.

    Your task is to find the students with maximum score and print his/her name. If there is tie, print all the names in ascending alphabetical order
'''
'''
Sample Input
1
5
Sam 40.08
Riya 30.7
Harry 41
Anne 35.2
Peter 36.6

Sample Output
Harry
'''
#temporary list for storing stuff
fin =[]
for i in range(int(input())):
    # a dictionary for each testcase
    ls ={}
    n = int(input())
    for a in range(n):
        name,score = input().split()
        ls[name] =score
        #sorting the dictionary on basis of key and storing it as a list
        ls1 = sorted(ls.items(),key=lambda kv:(kv[0],kv[1]))
    # Storing it as a new sorted dictionary
    finn ={k:v for (k,v) in ls1}
    # logic for finding the key in a dictionary when given a value
    for k,v in finn.items():
        if max(finn.values())==v:
            print(k)
