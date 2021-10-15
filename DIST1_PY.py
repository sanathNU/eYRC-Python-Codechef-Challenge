# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:59:13 2021

@author: FranticUser
"""

'''Created for CodeChef problem DIST1_PY
Problem Statement:
    Given 2 points (x1,y1) and (x2,y2), where x1, x2 are x-coordinates and y1, y2 are y-coordinates of the points.

    Your task is to compute the Euclidean distance between them.

    It calls the function compute_distance(). Your task is to complete the function.

The distance computed should be precise up to 2 decimal places.
'''
ls = []
for i in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    dist = float(pow(pow(x2-x1,2)+pow(y2-y1,2),0.5))
    ls.append(dist)

for items in ls:
    print('Distance: %.2f'%items)
    