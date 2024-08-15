# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
# n=5
# for i in range (n):
#     for j in range(n):
#             print((i,j),end=' ')
#
#     print()

'''
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or j==n-1 or i==0:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''


# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
*       * 
  *   *   
    *     
  *   *   
*       * 
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==(n-1)//2 or j==(n-1)//2:    #i==n//2 or j==n//2
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
    *     
    *     
* * * * * 
    *     
    *   
'''
# n=15
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or i==n-1 or j==0 or i==j or i +j==n-1 or i==n//2 or j==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
* * * * * * * * * * * * * * * 
* *           *           * * 
*   *         *         *   * 
*     *       *       *     * 
*       *     *     *       * 
*         *   *   *         * 
*           * * *           * 
* * * * * * * * * * * * * * * 
*           * * *           * 
*         *   *   *         * 
*       *     *     *       * 
*     *       *       *     * 
*   *         *         *   * 
* *           *           * * 
* * * * * * * * * * * * * * * 
'''

# n=5
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*        
* *       
* * *     
* * * *   
* * * * * 
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n//2 or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
*         
* * * * * 
*         
* * * * * 
'''

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0  or j==0 or i==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
*         
* * * * * 
*         
*  
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n//2 or j==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
*       * 
*       * 
* * * * * 
*       * 
*       * 
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i ==n-1 or j==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
    *     
    *     
    *     
* * * * * 
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i ==n-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
*         
*         
*         
*         
* * * * * 
'''





# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=5
# for i in range (1,n+1):
#     for j in range(i):
#         print(i,end=' ')
#     print()






# 1
# 1 2
# 1 2  3
# 1 2  3  4
# 1 2  3  4  5

# n=5
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()








# ##  Variable scopes
#
# #    Global variable:
# #A variable created in global namespace i.e., outside a function.
# #It can only be accessed inside a function but cannot be modified.
# #In order to modify a global variable inside a function then we have
# #     to use a keyword called 'global'
#
# #Ex:
# a = 10
# def func():
#     global a
#     a += 1
#
#
# #   Local variable:
# #A variable which is created inside a function is called a local
# #    variable and it can not be accessed outside the function.
#
# #ex:
# def func():
#     a = 10
#
# #   Nonlocal scopes:
# #Non local scopes are those which are neither local nor global.
# #If a nested function has to access and modify the variable of
# #outer function, nonlocal keyword should be used....
# #Ex:
# def func():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 1
#

#
# #global
# #function using global variables
# a = 56
# b = 45
# def display():
#     print(a+b)
#
# display()    #101
# print(a+b)   #101
#
#
# a = 56
# def func():
#     a = 25
#     b = 67
#     print("inside func, a is ", a)
#
# print("before func call, a is ", a)   #56
# func()                                #25
# print("after func call, a is ", a)    #56
#
#
# a = 56                #Global variable
# def func():
#     a = 25            #Local variable
#     b = 67
#     print("inside func, a is ", a)
#
# print("before func call, a is ", a)   #56
# func()                                #25
# print("after func call, a is ", a)    #56


# #function trying to modify global variables.
# a = 56
# b = 45
# def display():
#     a = 12
#     print(a+b)    #we can not modify here
#
# display()      #57
# print(a+b)      #101
#
#
# #function trying to modify global variable using global keyword.
# a = 56
# b = 45
# def display():
#     global a
#     a = 12
#     print(a+b)
#
# display()       #57
# print(a+b)      #57
#
#
##Updating global variables  (Example)
# city: Local city,  person: dinga, currency: burpee
# country: Global, person: dinga, currency: rupee

# dinga: currency = 500 burpee's, currency = 200 rupees

# currency= 200
# def func():
#     global currency
#     currency += 500
#     print(currency)
#
# print(currency)           #200
# func()                    #700
# print(currency)           #700


# WAP to count how many times that given function is ecxecuted.
# c = 0
# def add(a, b):
#     global c
#     print(a+b)
#     c +=  1
#     print(f"{c} times executed")
#
# add(6, 5)     # o/p: 11
#       1 times executed
# add(7, 8)    #o/p: 15
#                    2 times executed
#
##
# nonlocal
# a = 56
# def func():
#     global a
#     a = 66
#     b = 54
#     print("func", a)
#     def inner():
#         nonlocal b
#         b = 65
#         print("inner", b)
#
#     inner()
#     print("outside", b)
#
#
# func()




