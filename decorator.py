'''
a decorator takes the function and add  some features and  return the function
without modifying the original function
#-------------------------   or  ------------------------
adding new features for the existing function with out modifying the existing function



#syntax:
def decorator_name(func):
    def inner_function(*args,**kwargs):
            #statement
            func(*args,**kwargs)
    return inner_function

@decorator_name
def function_name(*args,**kwargs):
        #statement

'''

#wap to print a msg before exicuting the function
#-----------------------------------------------------------
# def outer(func):
#     def inner(a,b):
#         print('you got  the output like :',end=' ')
#         func(a,b)
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# @outer
# def sub(a,b):
#     print(a-b)
# add(4,5)
# sub(5,4)
#wap to print a wishing message before exicuting the function by using *args and **kwargs
#args--> it accept only positional argument
#**kwargs --> it will accept only keyword argument
# def add(*args):
#     print(type(args))
# add(1,2,3,4,5)  <tuple>
# def add(**kwargs):
#     print(*kwargs)
# add(a=4,b=3,c=5)   <dictionary>

# def sample(func):
#     def inner(*args,**kwargs):
#         print('good morning your numbers are:',end=' ')
#         func(*args,**kwargs)
#     return inner
# @sample
# def demo(*args,**kwargs):
#     print(f'args:-{args},kwargs:-{kwargs}')
# demo(1,2,3,4,a=5,b=6,c=7,d=8)
#o/p-->good morning your numbers are: args:-(1, 2, 3, 4),kwargs:-{'a': 5, 'b': 6, 'c': 7, 'd': 8}

#-------------------------------------------------------------------------------------------------
#wap to print whising msg before exicuting the function and print the sum of args and kwargs
#-------------------------------------------------------------------------------------------------
# def sample(func):
#     def inner(*args,**kwargs):
#         print('good morning your numbers are:',end=' ')
#         func(*args,**kwargs)
#     return inner
# @sample
# def demo(*args,**kwargs):
#     print(f'args:-{sum(args)},kwargs:-{sum(kwargs.values())}')
# demo(1,2,3,4,a=5,b=6,c=7,d=8)


#wap to delay the function for 5 sec after printing the msg

# from time import sleep
# def outer(func):
#     def inner(*args,**kwargs):
#         print('good morning:',end=' ')
#         sleep(10)
#         func(*args ,**kwargs)
#     return inner
# @outer
# def add(*args,**kwargs):
#     print(sum(args),max(kwargs.values()))
#
# add(1,2,3,4,5,a=9,b=99,c=199)

#o/p-->good morning: 15 199

#wap to  print the exicution time of a program after printing a msg
# from time import time,sleep
# def outer(func):
#     def inner(*args,**kwargs):
#         print('good morning:',end=' ')
#         start=time()
#         func(*args ,**kwargs)
#         stop=time()
#         print(f'the exicution time of the program {start},{stop} is{stop-start}')
#     return inner
# @outer
# def add(*args,**kwargs):
#     print(sum(args),max(kwargs.values()))
#     sleep(5)

# add(1,2,3,4,a=6,b=7,c=9)

#wap to check given mail id is valid or not by using decorator
# .com --> has to be there
# @ --> has to be the

# def v_email(func):
#     def inner(email):
#         if email.endswith('.com') and '@' in email:
#             func(email)
#         else:
#             print('error')
#     return inner
# @v_email
# def mail(email):
#     print(email)
# mail('dinga123@gmail.com')
# @v_email
# def yahoo(email):
#     print(email)
# yahoo('dingi@yahoo.com')



#wap to swap denominator and numerator if  denominator is 0 else do the
# division by using decorator
# def swap(func):
#     def inner(a,b):   #a=10    b=0
#         if b==0:
#             func(b,a)   #0,10
#         else:
#             func(a,b)
#     return inner
# @swap
# def div(a,b):
#     print(a//b)   #a==10    b=0   ==> a=0   b=10    0//10---0
# div(20,2)


# #wap to delay the exicution of the function by using parameterized decorator
# from time import sleep
# def n_delay(n):
#     def outer(func):
#         def inner(a,b):
#             sleep(n)
#             func(a,b)
#         return inner
#     return outer
# @n_delay(3)
# def add(a,b):
#     print(a+b)
# add(5,4)
#
# @n_delay(5)
# def sub(a,b):
#     print(a-b)
# sub(5,4)




#wap to run a function n no of times by using parameterized decorator

# def n_times(n):
#     def outer(func):
#         def inner(a,b):
#             for i in range(n):
#                 func(a,b)
#         return inner
#     return outer
# @n_times(4)
# def add(a,b):
#     print(a+b)
# add(4,3)
# @n_times(2)
# def mul(a,b):
#     print(a*b)
# mul(2,3)

#wap to give the acess only if the user is admin else throw error
# def acess(req_name,password):
#     def outer(func):
#         def inner(user_name,user_password,*args,**Kwargs):
#             if user_name==req_name and user_password == password:
#                 func(user_name,user_password)
#             else:
#                 print('error')
#         return inner
#     return outer
# @acess('admin','admin')
# def login(user_name,user_password):
#     print('welcome admin ')
# login('admin','admin')
#
# @acess('dev','dev')
# def dev_login(user_name,user_password):
#     print('welcome developer')
# dev_login('dev','dev')


#wap to assign 2 or more decorators for a single function
# def star(func):
#     def inner(*args,**kwargs):
#             print('*'*20)
#             func(*args,**kwargs)
#             print('*'*20)
#     return inner
# def percentage(func):
#     def inner(*args,**kwargs):
#         print('%'*8)
#         func(*args,**kwargs)
#         print('%'*8)
#     return inner
# def doller(func):
#     def inner(*args,**kwargs):
#         print('$'*5)
#         func(*args,**kwargs)
#         print('$'*5)
#     return inner
# @star
# @percentage
# @doller
# def greet(msg):
#     print(msg)
# greet('hello')

'''
********************
%%%%%%%%
$$$$$
hello
$$$$$
%%%%%%%%
********************
'''

















