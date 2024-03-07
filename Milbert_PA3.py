# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:41:41 2024

@author: HSMilbert
"""

import numpy as np
from numpy import *

#Part 1, number 4
func_1= np.poly1d([2, 3, 0, 1])
print(func_1)
#evaluate at x=2
func_eval_1 = polyval(func_1,2)
print(f'Function evaluated at 2 is {func_eval_1}')
print()

#Number 5
func_2 = np.poly1d([1, 0, 1])
print(func_2)
#Calc Deriv
deriv_func2 = np.polyder(func_2)
print(f'The derivative of function 2 is {deriv_func2}')
print()
#Eval deriv at 1
deriv_func2_eval = polyval(deriv_func2, 1)
print(f'The derivative evaluated at 1 is {deriv_func2_eval}')
#%%
#Part 2
import numpy as np
from numpy import *

#Create function and x1 value
coeff_list = []
polynomial = input('Enter the coefficients of your polynomial, ex: if it is x^2 + 3x - 2 --> enter 1, 3, -2: ')
list_nums = polynomial.split(',')
#loop through input string and add just # values to coeff_list
for num in list_nums:
    coeff = int(num)
    coeff_list.append(coeff)
#Create function and and x1 value - these are inputs for newtons_meth
func = np.poly1d(coeff_list)
x1 = int((input('Enter a x1 value: ')))

def newtons_meth(func, x1):
    #Calc deriv and x_n value 
    deriv = np.polyder(func)
    x_n = x1 - ((polyval(func, x1)) / (polyval(deriv, x1)))
    print(round(x_n, 3))
    if round(x_n,3) != round(x1,3):
        return newtons_meth(func, x_n)
    else:
        roots_list = []
        #Enter items calculated by numpy into list b/c numpy outputs roots of 3 and 2 as a list [3. 2.] and I thought that was confusing 
        for item in np.roots(func):
            #Python wanted me to use np.round b/c for cases like (x-2)^2 it doesn't like normal the round() fcn
            roots_list.append(np.round(item,3))
        #Print root found from newtons_meth and numpy roots
        print(f'One root is {round(x1, 1)}')
        print(f'Numpy calculated the root(s) to be {roots_list}')
        
    
newtons_meth(func, x1)
