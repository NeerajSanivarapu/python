#it is a block of code or set of instructions which is used to
# perform some specific task  when ever we called

#2. function makes the code more optimise

# syntax

# def function_name(parameters):    #function declaration
#     statement1
#     statement2
#     return data
# function_name(arguments)       #function calling


#syntax for return

# def  function_name(parameters):
    # return data1,data2,..........


#WAF to add 2 numbers
# def add(a,b):   #declaration
#     print(f'the sum of the given {a}, {b} numbers is:{a+b}')
# add(3,2)    #calling

#WAF to add 2 numbers and return the output
# def add(a,b):   #declaration
#     w=a+b
#     return w
# q=add(3,2)    #calling
# print(q)

# def add(a,b):
#     return a+b
# print(add(4,5))


# def add(a,b):
#     return (f'the square of {a} is {a**2} and {b} is {b**2}')
# print(add(3,4))
#WAF to count how many values are present in a given list without using len function

# def length(lst):
#     c=0
#     for i in lst:
#         c+=1
#     return c
# a=[1,2,3,4,5,6,7,8,9,10]
# print(length(a))

#o/p==> 10

#WAF to check given number is having even length or odd length if it
# is a even length return hello else return bye

# def number(a):
#     c=0
#     # t=len(str(a))    # by using typecasting
#------------------
# without using type casting
#     while a>0:   #0
#         v=a%10  #3
#         c+=1
#         a//=10   #123
#------------------

#     if c%2==0:
#         return 'hello'
#     else:
#         return 'BYE'
# print(number(123456789))

#WAF to check given string is palindrome or not if it is a palindrome
# return True else return False
# def is_palindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('malayalam'))    #True
# print(is_palindrome('amma'))     #True
# print(is_palindrome('hello'))     #False

# create a calculator by taking input from the user which operator has to perform
# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def floor_div(a,b):
#     print(a//b)
# def true_div(a,b):
#     print(a/b)
# a=int(input('enter the first number :'))
# b=int(input('enter second number:'))
# print('choose any one of the below :'
#       '\n +'
#       ' \n -'
#       ' \n / '
#       '\n // '
#       '\n * ')
# op=input('enter the option:')    #+
# if op=='+':
#     add(a,b)
# elif op=='-':
#     sub(a,b)
# elif op=='/':
#     true_div(a,b)
# elif op=='//':
#     floor_div(a,b)
# elif op=='*':
#     mul(a,b)
# else:
#     print('invalid operator')

#assignment
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#WAF to check the  position of a specified element in a collection
# i/p  function_name('qspiders','p') ==>2

# def sample(value,element):
#     #value ='qspiders'n    #elements =='p'
#     for i ,j in enumerate(value):
# #         i--index      # j =elements
#         if j==element:
#             return i
#     return 'not present'
# print(sample('qspiders','z'))

#WAF to check given list is homogeneous or not

# def homo(lst):
#     for i in lst:   #[1,2,3,'hi',5]
#         if type(lst[0])== type(i):
#             continue    #pass
#         else:
#             return 'hetrogeneous'
#     return 'homogeneous'
#
# print(homo([1,2,3,4,5,6]))

#WAF to check how many upper case ,lower case ,numbers,special characters
# are present in a given string

# def checking(str):
#     u=0
#     l=0
#     n=0
#     sp=0
#     for i in str:
#         if 'A'<=i<='Z':
#             u+=1
#         elif 'a'<=i<='z':
#             l+=1
#         elif '0'<=i<='9':
#             n+=1
#         else:
#             sp+=1
#     return u,l,n,sp
# print(checking('Hello123@'))


# !!!!!!!!!!!!!!!!!    TYPES OF ARGUMENTS !!!!!!!!!!!!!!!!!!

# def function_name(parameters):    #function declaration
#     statement1
#     statement2
#     return data
# function_name(arguments)       #function calling

# 1.positional arguments
# def demo(name,age):
#     print(f'your name is {name} and your age is {age}')
# demo('ram',22)
# # o/p==>   your name is ram and your age is 22
# demo(22,'ram')
#o/p==>  your name is 22 and your age is ram

# 2.keyword arguments

# def demo(name,age):
#     print(f'your name is {name} and your age is {age}')
# # demo('ram',23)    #positional
#
# demo(name='ram',age=23)
# # o/p==>   your name is ram and your age is 23
# demo(age=23,name='ram')
# o/p==>   your name is ram and your age is 23

# 3.combination of positional and keyword  arguments

# def add(name ,age ,phno,designation):
#     print(f'hi {name} your age {age} and phno {phno} and designation is{designation}')
# # add('ram',23,1234567890,'clerk')
# # add(name='ram',phno=12345678,designation='clerk',age=23)
# add('ram',23,designation='clerk',phno=13345565)
#
# #o/p==> hi ram your age 23 and phno 13345565 and designation isclerk
#
# add(name='ram',age=23,'clerk',13345565)

# o/p==>   SyntaxError: positional argument follows keyword argument


# 4.only positional arguments  (/)
# def add(name,age,phno,designation):
#     print(f'hi {name} your age {age} and phno {phno} and designation is{designation}')
#
# def add(a,b,c,d,/):
#     print(a+b+c+d)
# # add(10,20,30,40)
# add(a=10,b=1,c=12,d=39)

# o/p==> TypeError: add() got some positional-only arguments passed as keyword
# arguments: 'a, b, c, d'

# add(10,20,c=40,d=60)

# TypeError: add() got some positional-only arguments passed as keyword arguments: 'c, d'

# 5.only keyword arguments  (*)

# def add(*,a,b,c,d):
#     print(a+b+c+d)
# add(a=10,b=20,c=30,d=40)

# add(10,20,30,40)
# o/p==> TypeError: add() takes 0 positional arguments but 4 were given


# 6.combination of positional and keyword  arguments

# def add(a,b,/,*,c,d):      #/      #*
#     print(a+b+c+d)

# # add(10,20,c=30,d=40)
# add(10,20,30,d=40)
# # o/p==>TypeError: add() takes 2 positional arguments but 3 positional arguments
# # (and 1 keyword-only argument) were given
#
# add(a=10,20,c=30,d=40)
#o/p==  SyntaxError: positional argument follows keyword argument

# 7.variable positional arguments   (*args)
# def add(*args):    #packing
#     print(args)
#     print(*args)     #unpacking
#     s=0
#     for i in args:
#        s+=i
#     print(s)
# add(1,2,3,4,5,6,7)
# add(1,2,3,4,d=10,f=30)
# TypeError: add() got an unexpected keyword argument 'd'

# 8.variable keyword arguments       (**kwargs)
# def add(**kwargs):   #packing into a dict
#     print(kwargs)   #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
#     print(*kwargs) #unpacking      #a b c d e
#     for i ,j in kwargs.items():
#         print((i,j))      #('a', 10)
# #                           ('b', 20)
# #                           ('c', 30)
# #                           ('d', 40)
# #                           ('e', 50)
# add(a=10,b=20,c=30,d=40,e=50)


#combination of *args and **kwargs

# def add(*args,**kwargs):
#     print(f'the output of *args is {args}')    #the output of *args is (10, 20, 30)
#     print(f'the output of **kwargs is {kwargs}')   #  the output of **kwargs is {'c': 40, 'd': 50}
# add(10,20,30,c=40,d=50)



#WAF to check how many times given character is repeated
# i/p   function_name('malayalam','a') ===>o/p  -->   4
# def rep(name,value):
#     c=0
#     for i in name:
#          if i==value:
#              c+=1
#     print(c)
# rep('malayalam','a')

# def in_built(name,value):
#     return name.count(value)
# print(in_built('malayalam','a'))

#WAF to convert upper case into lower case and lower case into uppercase
# with out using string methods

# def convert(name):
#     res=''
#     for i in name :
#         if 'A'<=i<='Z':
#             res+=chr(ord(i)+32)
#         else:
#             res+=chr(ord(i)-32)
#
#     return res
# print(convert('DinGa'))

#WAF to  create a dictionary with a key as element and value as its power of index
# if element is even else power of the element

# def create(element):
#     dic={}
#     for i,j in enumerate(element):
#         if j%2==0:
#             dic[j]=j**i
#         else:
#             dic[j]=j**j
#     print(dic)
# create([1,2,3,4,5,6,7])
# #o/p==> {1: 1, 2: 2, 3: 27, 4: 64, 5: 3125, 6: 7776, 7: 823543}


#default parameters


# def add(a,b,c=0,d=0):
#     print(a+b+c+d)
# add(4,5,6,7)   #4+5+6+7 ==> 22
#
# add(4,5)    #4+5+0+0==9
# add(4)    #error

# db={'dinga':1000,'dingi':200}
# dbp={'dinga':1234}
# def login():
#     name=input('enter your name:')
#     print(f'welcome   {name}')
#     t=input('enter y if you have account in this bank already :')
#     if t.lower() =='y':
#         Home(name)
#     else:
#         customer_signup(name)
#
# def customer_signup(name):
#     if name not in db:
#         amount=int(input('enter the amount :'))
#         pin=int(input('enter your pin :'))
#         db[name]=amount
#         dbp[name]=pin
#         print('thank your for creating account in our bank')
#         to_continue(name)
#     else:
#         print('user already exist ')
#
#
# def Home(name):
#     if name in db:
#         pin=int(input('enter your pin :'))
#         if pin == dbp[name]:
#             print('choose the options 1. withdraw   2. deposit    3.balance  4.trasnfer')
#             l=int(input('enter your option'))
#             if l==1:
#                 withdraw(name)
#
#             elif l==2:
#                 deposit(name)
#
#             elif l==3:
#                 balance(name)
#
#             elif l==4:
#                 transfer(name)
#
#             else:
#                 print('invaid option')
#         else:
#             print('invalid pin')
#     else:
#         print('invalid user name')
#
# def withdraw(name):
#     amount=int(input('enter the amount to witdraw'))
#     if amount<=db[name]:
#         db[name] -=amount
#         print(f'{amount} RS is debited from your account available balane is {db[name]} RS')
#         to_continue(name)
#     else:
#         print('insufficinet funds')
# def deposit(name):
#     amount=int(input('enter the amount to deposit :'))
#     db[name]+=amount
#     print(f'{amount} got credited into your account available balance is {db[name]}')
#     to_continue(name)
# def balance(name):
#     print(f'available balance is {db[name]}')
#     to_continue(name)
# def transfer(name):
#     reciver_name=input('enter the reciver name')
#     if reciver_name in db:
#         amount=int(input('enter the amount to transfer'))
#         if amount <=db[name]:
#             db[name]-=amount
#             db[reciver_name]+=amount
#             print(f'{amount} succesfully trasfterd to {reciver_name}')
#         else:
#             print('insufficinet funds to transfer')
#     else:
#         print(f'{reciver_name} not exists')
#     to_continue(name)
# def to_continue(name):
#     t=input('enter y if you want to continue')
#     if t.lower()=='y':
#         Home(name)
#     else:
#         print('thank you for visiting the bank')
#
# login()






