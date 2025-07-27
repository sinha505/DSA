# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 09:06:23 2025

@author: sinhsant
"""


arr = [0, 2, 5, 4, 6, 17]
target = 10

def twoSum(arr, target):
    aset = set(arr)
    for num in arr:
        balance = target - num
        if balance in aset and balance !=num:
            return(num, balance)
    return("none")

twoSum(arr, target)

# difference between & in python, C++, Java, etc.
a_dict = dict(enumerate(arr))
a_set = set(arr)


# The complexity of the below algorithm is O(n).
# Explanation:
# - dict(enumerate(A)) creates a dictionary in O(n) time.
# - The for loop iterates over A once (O(n)).
# - The 'in' operation on a dictionary is O(1) on average.
# So, the total time complexity is O(n).

A = [0, 2, 4, 5, 6, 17]
target = 10
V = dict(enumerate(A))  # can also use A

for i in range(len(A)):
    balance = target - A[i]
    if (balance in A) and (balance != A[i]):
        print(A[i], balance)
        break
        
        
        
        
