#1. wap to print 1 to 5 numbers
# i=1
# while i<=5:
#     print(i,end=' ')
#     i=i+1
# o/p :-1 2 3 4 5
from enum import property

#2.wap to print 1 to 10 numbers
# i=1
# while i <=10:
#     print(i,end=' ')
#     i+=1
# o/p:- 1 2 3 4 5 6 7 8 9 10


#3. wap to print hello python  5 times
# i=1
# while i <=5:
#     print(f'{i}. hello python')
#     i+=1
# o/p:-
# 1. hello python
# 2. hello python
# 3. hello python
# 4. hello python
# 5. hello python

#4.wap to print 10 to 1  numbers
# i=10
# while i>0:
#     print(i,end=' ')
#     i-=1  #i=i-1
#o/p :- 10 9 8 7 6 5 4 3 2 1

#5.wap to print even numbers from 1 to 10

# i=1
# while i <=10:
#     if i %2==0:
#         print(i,end=' ')
#     i+=1

#o/p :-   2 4 6 8 10

# METHOD --2

# i=2
# while i <=10:
#     print(i,end=' ')
#     i+=2


#6.wap to print  odd numbers from 1 to n
# n=int(input('enter the number :'))
# i=1
# while i<=n:
#     if i %2!=0 :      #i%2==1
#         print(i,end =' ')
#     i+=1

# o/p:-

# enter the number :10
# 1 3 5 7 9

#7.wap to n th table
# o/p : 15 *1 =15
# i=1
# n=int(input('enter the number:'))
# while i<=10:
#     print(f'{n} * {i} = {n*i}')
#     i+=1

#o/p
# 15 * 1 =15
# 15 * 2 =30
# ...

# 8.wap to reverse the given number(with out using type casting )
# num=int(input('enter the number'))
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print(rev)


# 9.wap to check given number is palindrome
# a=int(input('enter the number:'))   #121
# num=a     #121
# rev=0
# while a>0:
#     rev=rev*10+a%10     #1*10  =10       #10+2=12   12*10  =120    120+1=121
#     a=a//10      #12         #1          #0
# if num==rev:
#     print('palindrome')
# else:
#     print('not a palindrome')

# #10.wap to traverse through a string
# s='hello'
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1

#11.wap to reverse a string


# s=input('enter your name :')
# i=0
# res=''
# while i <len(s):
#     res=s[i]+res
#     i+=1
# print(res)

#method ---2

# s=input('enter your name :')
# i=1
# res=''
# while i <=len(s):
#     res+=s[-i]
#     i+=1
# print(res)


#wap to check whether given string is paindrome or not
# s=input('enter your string')
# i=0
# res=''
# while i <len(s):
#     res=s[i]+res
#     i+=1
# if s==res:
#     print('palindrome ')
# else:
#     print('not a palindrome')


#wap to convert uppercase letters into lower and lower case
# letters into upper without using string methods
#hElLo    ===> o/p    HeLlO

#by using string methods

# s=input('enter your string:')
# i=0
# res=''
# while i <len(s):
#     if s[i].isupper():
#         res=res+s[i].lower()
#     else:
#         res=res+s[i].upper()
#     i+=1
# print(res)


# s=input('enter your string')
# i=0
# res=''
# while i<len(s):
#     if ord('A')<=ord(s[i])<=ord('Z'):
#         res=res+chr(ord(s[i])+32)
#     else:
#         res = res + chr(ord(s[i]) - 32)
#     i+=1
# print(res)



#fibonacci series
# n=int(input('enter how many fibonocci series you want :'))
# a=0
# b=1
# print(a,b ,end=' ')
# i=1
# while i<=n-2:
#     c=a+ b    #0  +1  =1
#     print(c,end=' ')
#     a=b
#     b=c
#     i+=1


#wap to print factorial of a given number
# n=5
# i=1
# fact=1
# while i <=n:
#     fact=fact*i
#     i+=1
# print(fact)

# n=5
# fact=1
# while n>0:
#     fact=fact*n
#     n-=1
# print(fact)

#wap to print perfect square or not
# n=int(input('enter the number:'))
# temp=n**0.5
# if temp == temp//1:
#     print('perfect square')
# else:
#     print('not a perfect square')

#wap to print given number is  perfect number or not

# n=int(input('enter your number:'))
# i=1
# sum=0
# while  i <=n//2:   #i<n//2+1     #i<n
#     if n%i==0:
#         sum+=i  #sum=sum+i
#     i+=1
# if n==sum:
#     print('prefect number')
# else:
#     print('not a perfect number')


#wap to print sum of the digits present a number

# n=int(input('enter your number:'))
# sum=0
# while n>0:
#     sum=sum+n%10     # 0+4=4
#     n=n//10      #1234//10 => 123
# print(sum)

#harshad number

# n=int(input('enter your number:'))
# num=n
# sum=0
# while n>0:
#     sum+=n%10
#     n//=10
# if num%sum==0:
#     print('it is a harshad number')
# else:
#     print('not a harshad number')

#wap to check whether given number is strong number or not
# num=int(input('enter your number'))
# n=num
# sum=0
# while num>0:
#     temp=num%10
#     fact =1
#     while temp>0:
#         fact *=temp
#         temp-=1
#     sum+=fact
#     num//=10
# if n==sum:
#     print('strong number ')
# else:
#     print('not a strong number')

#wap to traverse through a list  and check whether the word is
# having even length or odd if it is even add to a new list as
# it is if it a odd length reverse the word  and add to a list

# lst=['facebook','insta','whatsapp','twitter','apple','grapes']
# res=[]
# i=0
# while i<len(lst):
#     if len(lst[i]) % 2==0:   #lst[0]   ==>8 %2==0
#         res.append(lst[i])
#     else:
#         res.append(lst[i][::-1])
#     i+=1
# print(res)


# wap to traverse through a list  and check whether the word is
#starting with vowel or not if it is starting with vowel add to new
# list as it is if it consonent reverse the word  and add to a list
#
# lst = ['facebook', 'insta', 'whatsapp', 'twitter', 'apple', 'grapes']
# res=[]
# i=0
# while i<len(lst):
#     if lst[i][0] in 'aeiouAEIOU':
#         res.append(lst[i])
#     else:
#         res.append(lst[i][::-1])
#     i+=1
# print(res)

#o/p====>   ['koobecaf', 'insta', 'ppastahw', 'rettiwt', 'apple', 'separg']

#wap to traverse through a list and create a new list with a tuple of word and
# its index if the given word is even length else word and length of the word
# lst = ['facebook', 'insta', 'whatsapp', 'twitter', 'apple', 'grapes']
# res=[]
# i=0
# while i <len(lst):
#     if len(lst[i])%2==0:
#         res.append((lst[i],i))
#     else:
#         res.append( ( lst[i],len(lst[i]) ) )
#     i+=1
# print(res)

#o/p==>   [('facebook', 0), ('insta', 5), ('whatsapp', 2), ('twitter', 7),
# ('apple', 5), ('grapes', 5)]

#wap to  create a list by word and reverse word pair inside a tuple
# lst = ['facebook', 'insta', 'whatsapp', 'twitter', 'apple', 'grapes']
# res=[]
# i=0
# while i <len(lst):
#     res.append((lst[i],lst[i][::-1]))
#     i+=1
# print(res)

#o/p====>   [('facebook', 'koobecaf'), ('insta', 'atsni'),
# ('whatsapp', 'ppastahw'), ('twitter', 'rettiwt'),
# ('apple', 'elppa'), ('grapes', 'separg')]

#wap to create a dictionary  key as word value as index of the word
# lst = ['facebook', 'insta', 'whatsapp', 'twitter', 'apple', 'grapes']
# dic={}
# i=0
# while i <len(lst):
#     # dic['key']=value
#     dic[lst[i]]=i
#     i+=1
# print(dic)
# o/p==>{'facebook': 0, 'insta': 1, 'whatsapp': 2,
# 'twitter': 3, 'apple': 4, 'grapes': 5}


#wap to create a dictionary  with key as word and value
# as index if it is even length else word and length if it is
# odd length
# lst = ['facebook', 'insta', 'whatsapp', 'twitter', 'apple', 'grapes']
# dic={}
# i=0
# while i <len(lst):
#     if len(lst[i])%2==0:
#         dic[lst[i]]=i
#     else:
#         dic[lst[i]]=len(lst[i])
#     i+=1
# print(dic)
# {'facebook': 0, 'insta': 5, 'whatsapp': 2, 'twitter': 7, 'apple': 5, 'grapes': 5}

#wap to print a dictionary with key as number and value as
# square of the number if the given number is  even else cube of the number
# lst=[1,2,3,4,5,6,7,8,9]
# dic={}
# i=0
# while i <len(lst):
#     if lst[i]%2==0:
#         dic[lst[i]]=lst[i]**2
#     else:
#         dic[lst[i]]=lst[i]**3
#     i+=1
# print(dic)

#o/p==>{1: 1, 2: 4, 3: 27, 4: 16, 5: 125, 6: 36, 7: 343, 8: 64, 9: 729}