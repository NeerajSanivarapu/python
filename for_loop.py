# lst=[1,2,3,4,5]
# i=0
# while i <len(lst):
#    print(i**2)
#    i+=1

# for i in lst:
#     print(i**2,end=' ')

# o/p=>1 4 9 16 25

# wap to print squares of the number's present in a list  if
# it is even number
# lst=[1,2,3,4,5,6,7,8]
# for i in lst:
#     if i%2==0:
#         print(i**2,end=' ')
# o/p==>4 16 36 64

#wap to print data and what type of data it is

# lst=[1,1.2,True,2+3j,'hello',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3}]
# for i in lst:
#     print(f'{i} is a type of {str(type(i))[7:-1]}')
#
# o/p==>
# 1 is a type of 'int'
# 1.2 is a type of 'float'
# True is a type of 'bool'
# (2+3j) is a type of 'complex'
# hello is a type of 'str'
# [1, 2, 3] is a type of 'list'
# (1, 2, 3) is a type of 'tuple'
# {1, 2, 3} is a type of 'set'
# {1: 1, 2: 2, 3: 3} is a type of 'dict'

# wap to create a list if the words starting with upper case
# lst=['Amazon','apple,','Flipkart','swiggy','Zomato','Big basket','blinkit']
# res=[]
# for i in lst:
#     if i[0].isupper():
#         res.append(i)
# print(res)

# for i in lst:
#     if ord('A')<=ord(i[0])<=ord('Z'):
#         res.append(i)
# print(res)

# for i in lst:
#     if 'A'<=i[0]<='Z':
#         res.append(i)
# print(res)

#wap to create a list with the words having  length morethan 6
# lst=['Amazon','apple,','Flipkart','swiggy','Zomato','Big basket','blinkit']
# res=[]
# for i in lst:
    # if len(i)>6:
    #     res.append(i)
# print(res)

# o/p==>['Flipkart', 'Big basket', 'blinkit']

#                                           RANGE()

#wap to print 1 to 10 numbers by using range function
# for i in range(1,11):
#     print(i)
#wap to print numbers from 10 to 1 by using range function
# for i in range(10,0,-1):
#     print(i)

#wap to check whether the user entered number is a prime number or not
#
# n=12
# for i in range(2,n):
#     if n%i==0:
#         print('not a prime number')
#         break
# else:
#     print('prime')

# for presentation wap to print prime numbers from 1 to 10
# n=[1,2,3,4,5,6,7,8,9,10]
# a=0
# while a<len(n):
#     for i in range(2,n[a]):
#         if n[a]%i==0:
#             break
#     else:
#         print(n[a],end=' ')
#     a+=1
#
# n=[1,2,3,4,5,6,7,8,9,10]
# for i in n:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=' ')

#wap to traverse through a set and create a dictionary with word
# and length pair
# s={'apple','bannana','grapes','orange','sun flower','mango'}
# dic={}
# for i in s:
#     # dic['keys']=value
#     dic[i]=len(i)
# print(dic)
# o/p==>{'mango': 5, 'grapes': 6, 'orange': 6, 'apple': 5, 'bannana': 7, 'sun flower': 10}

#with out declaring thE DICTIONARY

# lst=[]
# for i in s:
#     lst.append((i,len(i)))
# print(dict(lst))

#o/p==>{'mango': 5, 'bannana': 7, 'sun flower': 10, 'apple': 5, 'grapes': 6, 'orange': 6}

#WAP TO CREATE A DICTIONARY OF NAME AND SALARY PAIR BY GIVING 15 % HIKE
# name=['dinga','dingi','manga','mangi','sanga','sangi']
# sal=[1000,2000,3000,1500,2300,3210]
# dic={}
# for i in range(len(name)):   #0  to  5
#     dic[name[i]]=sal[i]+sal[i]*15//100
# print(dic)
# o/p=>{'dinga': 1150, 'dingi': 2300, 'manga': 3450, 'mangi': 1725,
# 'sanga': 2645, 'sangi': 3691}

#wap to create a dictionary by seprating flowers fruits and plants
# with key as flowers and values as list of flowers and so on....
# s=['rose flower','jasmine flower','apple fruit','grapes fruit','neem plant',
#    'orange fruit','money plant']
#
# #dic ={'flower:[rose,jasmine],'fruit:['apple','grapes']}
# dic={}
# for i in  s:
#   value,key =i.split()   #jasmine    flower
#   if key not in dic:
#       dic[key]=[value]
#   else:
#       dic[key].append(value)
#       #dic[key]+=[value]
# print(dic)

#o/p=>{'flower': ['rose', 'jasmine'], 'fruit': ['apple', 'grapes', 'orange'],
# 'plant': ['neem', 'money']}

#wap to create a dictionary with a key as type of data and values as elements
# a=[2,3,2.3,True,False,'hello','bye',4.55]
# dic={}
# for i in a:
#     #type(i)===>  int      8 -2
#     t=str(type(i))[8:-2]
#                                 #t =int
#     if t not in dic:
#         dic[t]=[i]
#     else:
#         dic[t]+=[i]
# print(dic)

#o/p==>{'int': [2, 3], 'float': [2.3, 4.55], 'bool': [True, False], 'str': ['hello', 'bye']}

# wap to traverse through a dictionary and create a dictionary of fruit and its price
# if the price is even add 10 rupees if it is odd add 20 rs

# fruits={'apple':1000,'grapes':2345,'bannana':1267,'oranges':9874,'mango':7000}
# dic={}
# for i in fruits:
#     if fruits[i]%2==0:    #1000 %2==0
#         dic[i]=fruits[i]+10
#     else:
#         dic[i]=fruits[i]+20
# print(dic)

#o/p==>{'apple': 1010, 'grapes': 2365, 'bannana': 1287, 'oranges': 9884, 'mango': 7010}


#wap to print alphabets upper and lower from a to z

# for i in range(26):
#     print(chr(65+i),chr(97+i),sep=' ',end=' ')
#for i in range(26):
#     print(chr(65+i),end=' ')
# for j in range(26):
#     print(chr(97+j),end=' ')


#wap to check how many alphabets are present in  GIVEN string
# s='hello@123'
# c=0
# for i in s:
#     if i.isalpha():
#         c+=1
# print(c)
#@@@@@@@@@@@    METHOD-2  @@@@@@@@@@@@@@@@@@@@@@@@@@
#     if ord('A')<=ord(i.upper())<=ord('Z'):
#         c+=1
# print(c)
#@@@@@@@@@@@@@@   METHOD-3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     if 'A'<=i.upper()<='Z':
#         c+=1
# print(c)


#wap to count how many digits are present in a given string
# s='hello@123'
# c=0
# for i in s:
#    if i.isdigit():
#        c+=1
# print(c)


#     if ord('0')<=ord(i)<=ord('9'):
#         c+=1
# print(c)


    # if '0'<=i<='9':
    #     c+=1
# print(c)

#wap to print how many special characters are present in a given string
# s='hello@123 world@'
# c=0
# for i in s:   #h
#     if i.isalnum()==False:
#         c+=1
# print(c)

#wap to check the password is valid or not
# s='DInd@1'
# u_count=0
# l_count=0
# s_count=0
# n_count=0
# if len(s)>=8:
#     for i in s:
#         if 'A'<=i<='Z':
#             u_count+=1
#         elif 'a'<=i<='z':
#             l_count+=1
#         elif '0'<=i<='9':
#             n_count+=1
#         else:
#             s_count+=1
#     if u_count>=2 and l_count>=2 and s_count>=1 and n_count>=1:
#         print('valid password')
#     else:
#         print('invalid password')
# else:
#     print('invalid lenth')



# loop control statements

#1.break
#2.continue
#3.pass

# @@@@@@@@@@@@@@@  break
# for i in range(1,11):
#     if i ==8:
#         break
#     else:
#         print(i,end=' ')
# #o/p==>    1 2 3 4 5 6 7
#  @@@@@@@@@@@@@@@    continue
# for i in range(1,11):
#     if i ==8:
#         continue
#     else:
#         print(i,end=' ')
# #o/p==>    1 2 3 4 5 6 7 9 10
# @@@@@@@@@@@@@@@    pass
# age=18
# if age >17:
#     pass

#creating a list with user input

# lst=[]
# print('eneter your values and enter done one lsit is complited')
# while True:
#     a=input('enter the value')
#     if a.lower()=='done':
#         break
#     else:
#         lst.append(a)
# print(lst)


# s=set()
# print('enter the values and enter done')
# while True:
#     a=input('enter')
#     if a.lower()=='done':
#         break
#     else:
#         s.add(a)
# print(s)


#wap to create a dictionary by getting input from the user
# dic={}
# print('enter key and vLUES AND ENTER DONE ONCE DONE')
# while True:
#     key=input('enter the key')     #done
#     if key !='done':
#         value=input('enter the value')
#         dic[key]=value
#     else:
#         break
# print(dic)



#armstong number
# n=input('enter your number:')
# sum=0
# digits=len(n)
# for i in n:
#     sum+=int(i)**digits
# if sum==int(n):
#     print('armstong')
# else:
#     print('not')



#happy number
n=12
while n!=1 and n!=4:
    sum=0
    while n>0:
        num=n%10
        sum+=num**2
        n//=10
    n=sum
if n==1:
    print('happy number')
else:
    print('not a happy number')












































