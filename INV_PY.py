# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:51:00 2021

@author: FranticUser
"""

'''Created for CodeChef Problem INV_PY
Problem Definition
    Ash is tasked with maintaining an inventory list of all the items in a lab. The inventory list contains entries of all the items present in the lab along with its quantity. On daily basis items can be borrowed from the lab or new items can be added to the Lab. Hence Ash usually performs 2 operations on the inventory list:
    
    Adding items to the list
    Deleting items from the list
    Ash usually does this manually and would prefer to use a program to maintain the inventory list. Your task is to write a program that will help Ash.
    
    Consider there are N items in the lab initially. Therefore create a list L that will contain all the names of items (item_name) along with its quantity (item_quantity).
    
    Also, make provision for adding/deleting items to/from the list. The item name and its quantity along with the operation (ADD / DELETE) will be specified. You must take care of the following conditions while performing any of the operations on the list.
'''
'''
Sample Input
1
3
Servo 3
Drone 6
Board 7
3
ADD LEDs 4
DELETE Board 4
DELETE Servo 4

Sample Output
ADDED Item LEDs
DELETED Item Board
Item Servo could not be DELETED
Total Items in Inventory: 16
'''
#number of testcases
n = int(input())
for i in range(n):
    # looping over the testcases and storing the inventory data in an dictionary data structure
    nOfItems = int(input())
    invent ={}
    
    for a in range(nOfItems):
        item,count = input().split()
        invent[item] =int(count)
    
    # taking in the number of operations and storing each operation in a list
    nOfOps = int(input())
    lsOfOperations = [input().split() for b in range(nOfOps)]
    
    #parsing through each command and modifying the inventory according to that
    for items in  lsOfOperations:
        op,name,number = items
        
        if op=='ADD':
            if name in invent.keys():
                invent[name]+=int(number)
                print('UPDATED Item',name)
            else:
                invent[name]=int(number)
                print('ADDED Item',name)
        
        if op=='DELETE':
            if name in invent.keys():
                if int(number) < invent[name]:
                    invent[name]-=int(number)
                    print('DELETED Item',name)
                else:
                    print(name,'could not be DELETED')  
            else:
                print('Item',name,'does not exist')
    
    #Finally printing the total amount of items present in the inventory
    print('Total Items in Inventory:',sum(invent.values()))
    
