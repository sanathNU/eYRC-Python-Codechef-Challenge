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
'''
Sample Input
2
-1 0 5 0
2 1 6 -2

Sample Output
Distance: 6.00
Distance: 5.00
'''
#This is written according to the format given by codechef
# Import any required module/s
import math;

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):

    distance = 0
    distance=math.sqrt(((y2-y1)**2)+((x2-x1)**2))
    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places
    print("Distance: "+"{0:.2f}".format(distance))

# Main function
if __name__ == '__main__':

    # Take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the x1, y1, x2 and y2 values
    test=list()
    for _ in range(test_cases):
        test.append(list(map(int,input().split())))
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
    for cases in test:
        x1,y1,x2,y2=cases
        compute_distance(x1, y1, x2, y2)
