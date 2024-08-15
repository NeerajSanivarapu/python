# inbuilt methods
#1.type()
# a=10
# print(type(a))   #<class 'int'>
#2.id()
# a=10
# print(id(a))    #140727374846680
#3.dir()
#print(dir(str))
#4.help()
# help('str')
#5.len()
# s='hello'
# print(len(s))
#6.isidentifier()
# print('a1'.isidentifier())
#7.iskeyword()
# from  keyword import iskeyword
# print(iskeyword('None'))
#8.round()

# print(round(9.5))    #10
# print(round(9.32))   #9

#9.bin()

# print(bin(12))  #1100
# print(bin(-12))
#10.ord()
# print(ord('A'))
#11.chr()
# print(chr(65))
#12.input()
#input()
#13.output()
# print()
#14.range()

# for i in range(1,11):
#     print(i)

#15.divmod()
# print(divmod(12,2))   (6,0)
#16.abs()
# it is used to get the absalute value (with out having simbols)
# print(abs(2+3j))   #  3.605551275463989

#few_more_functions

#17.reversed()

# lst=[1,2,3,4,5]
# print(list(reversed(lst)))
# s='hello'
# print(list(reversed(s)))

# lt=[1,2.2,True,(2+3j),'hello']
# print(list(reversed(lt)))

#18.enumerate()
#syntax:
# enumerate(iterable,[start=])

#wap to print index and element
# n=['a','b','c','d']
# # for i in range(0,len(n)):
# #     print(i,n[i],sep=':',end=' ')
#
# for i ,j in enumerate(n):
#     print(i,j,sep=":",end=' ')
#
#
# for i ,j in enumerate(n,start=100):
#     print(i,j ,sep=':',end=' ')


#wap to print elements present in even index
# lst=['apple','mango','grapes','orange','bannana','dragonfruit']
# for i in range(2,len(lst),2):
#     print(lst[i])

# for i in range(2,len(lst)):
#     if  i %2==0:
#         print(lst[i])


# for i ,j in enumerate(lst):
#     # i ---> index         #j---> values
#     if i %2==0 and i!=0:
#         print(j)

#o/p:===>   grapes
#           bannana

# wap to print elements if the element present in even index and starting with vowel
# lst=['rapes','mango','apple','orange','bannana','dragonfruit']
# for i in  range(2,len(lst)):
#     if i %2==0 and lst[i][0] in 'aeiouAEIOU':
#         print(lst[i])

# for i ,j in enumerate(lst):
#     # i ==>index    j==>value
#     if i %2==0 and j[0] in 'aeiouAEIOU' and i!=0:
#         print(j)

# wap to print sum of the elements present in odd index if the number is even
# lst=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# # for i in range(1,len(lst),2):
# #    if  lst[i]%2==0:
# #        sum+=lst[i]
# # print(sum)

# for i ,j in enumerate(lst):
#     # i-->index     j-->values
#     if i %2==1  and j%2==0  and i!=0:
#         sum+=j
# print(sum)


#wap to check given number is xylem or pholem number
# i/p==> 1234
# n=1234
# num=n
# o_sum=0
# i_sum=0
# while n>0:
#     if num==n or n<=9:
#         o_sum+=n%10
#         n//=10
#     else:
#         i_sum+=n%10
#         n//=10
# if i_sum==o_sum:
#     print('xylem')
# else:
#     print('pholem')



#19.zip()
# syntax:
# zip(itterable1,itterable2,....)
#wap to create a list with the product of elements present in2 list's
# in the same index

#lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# res=[]
#res=[6,14,24,36,50]
# for i in range(len(lst1)):   #0
#     res.append(lst1[i]*lst2[i])
# print(res)

# for i ,j in zip(lst1,lst2):
#     # i ==>1       j==>6
#     res.append(i*j)
# print(res)


# lst1=[1,2,3,4,5]
# lst2=[1,2,3,4]
# lst3=[1,2,3,4,5]
# res=[]
# for i ,j,z in zip(lst1,lst2,lst3):
#     res.append(i*j*z)
# print(res)

#o/p==>[1, 8, 27, 64]

#wap to create a dictionary by taking elements from 2 lists
# lst=['a','b','c','d']  #keys
# lst1=[1,2,3,4]   #values
# dic={}
# for i in range(len(lst)):
#     dic[lst[i]]=lst1[i]
# print(dic)

# for i ,j in zip(lst,lst1):
#     dic[i]=j
# print(dic)

#o/p==>{'a': 1, 'b': 2, 'c': 3, 'd': 4}


#wap to create a dictionary by taking key from the first  list and values
# from the second list in reverse order

# lst1=['dinga','dingi','manga','mangi','sanga','sangi']
# lst2=[15,18,21,23,17,23]
# dic={}
# for i ,j in zip(lst1,lst2[::-1]):
#     dic[i]=j
# print(dic)

# for i ,j in zip(lst1,reversed(lst2)):
#     dic[i]=j
#
# print(dic)

#o/p==>{'dinga': 23, 'dingi': 17, 'manga': 23, 'mangi': 21, 'sanga': 18, 'sangi': 15}

#wap to creata 2 dictionary by taking key from first
# list and values from another 2 lists
# lst1=['a','b','c','d']
# lst2=[1,2,3,4]
# lst3=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# dic1={}
# dic2={}
# for i ,j,z in zip(lst1,lst2,lst3):
#     # i-->list1     j -->list2      z-->lsit3
#     dic1[i]=j
#     dic2[i]=z
# print(dic1)
# print(dic2)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}

#wap to create a dictionary by taking key from a string
# and values from a list in shuffle order
# s='hello'
# lst=[1,2,3,4,5]
# {'h':2,'e':4}

#20.zip_longest()
# from itertools import  zip_longest
# lst1=['a','b','c','d','e','f','g']
# lst2=[1,2,3]
# dic1={}
# for i,j in zip(lst1,lst2):
#     dic1[i]=j
# print(dic1)
# {'a': 1, 'b': 2, 'c': 3}

#========================================
# dic={}
# for i,j in zip_longest(lst1,lst2,fillvalue='dinga'):
#         dic[i]=j
# print(dic)

# wap to print name and sal with a hike of 25%  for thier actual salary
# if the person not earning salary print 0
# from itertools import zip_longest
# name=['dinga','dingi','manga','mangi','sanga','sangi']
# sal=[1000,2000,1300,2100]
# res={}
# for i ,j in zip_longest(name,sal,fillvalue=0):
#     res[i]=j+j*25//100
# print(res)

#wap to print company name and  country name in which it was started if country
# is not present    print not specified


# from itertools import zip_longest
# company=['apple','tata','mahindra','toyoto','kia','bmw']
# country=['usa','india','india','japan','korea']
# dic={}
# for i ,j in zip_longest(company,country,fillvalue='not specified'):
    # print(f'{i} is belongs to the {j}')
    # dic[i]=j
# print(dic)



#21.defaultdict()
#wap to check how many times element  is repeated
# from collections import defaultdict
# s='aabbccaabbc'
# # dic={}
# # for i in s:
# #     if i not in dic:
# #         dic[i]=1
# #     else:
# #         dic[i]+=1
# # print(dic)
# #o/p-->{'a': 4, 'b': 4, 'c': 3}
#
# d=defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)
#o/pdefaultdict(<class 'int'>, {'a': 4, 'b': 4, 'c': 3})


#syntax:
# from collections import defaultdict
        # dic=defaultdict(datatype)

# wap to  separate fruits ,vegetables,plants
# name=['apple fruit','grapes fruit','drum_stick vegetable','lady_finger vegetable',
#       'neem plant','thulasi plant','tomato vegetable']
# dic={}
# for i in name:
#     val,key =i.split()
#     if key not in dic:
#         dic[key]=[val]
#     else:
#         dic[key]+=[val]
#  print(dic)

#{'fruit': ['apple', 'grapes'],
# 'vegetable': ['drum_stick', 'lady_finger', 'tomato'], 'plant': ['neem', 'thulasi']}

# from collections import defaultdict
# d=defaultdict(list)
# for i in name:
#       val,key =i.split()
#       d[key]+=[val]
# print(d)

# defaultdict(<class 'list'>, {'fruit': ['apple', 'grapes'],
# 'vegetable': ['drum_stick', 'lady_finger', 'tomato'], 'plant': ['neem', 'thulasi']})




#
# n=10
# for i in range(n):
#     for j in range(0,n-i-1):
#         print(' ',end=' ')
#     for k in range(0,i+1):
#         print(' * ' ,end=' ')
#     print()
# for i in range(n-1):
#     for j in range(0,i+1):
#         print(' ',end=' ')
#     for k in range(0,n-i-1):
#         print(' * ' ,end=' ')
#     print()
#
# print('\n\n\n')


# i = 1
# k=0
# while i:
#     if k==0:
#         sp= ((n-i) * 2) * ' '
#         st= ' '.join((i) * '* ')
#         print(sp + st )
#         i += 1
#         if i == n:
#             k = 1
#     else:
#         sp = ((n - i) * 2) * ' '
#         st = ' '.join((i) * '* ')
#         print(sp + st)
#         i -= 1


# print('\n\n\n')
#
# for i in range(1, n-1):
#     sp= ((n-i-1) * 2) * ' '
#     st= ' '.join((i) * '* ')
#     print(sp + st )
# for i in range(n-1, 0, -1):
#     sp= ((n-i-1) * 2) * ' '
#     st= ' '.join((i) * '* ')
#     print(sp + st )









# from pandas import DataFrame
# #WAP to create a marks sheet using dataframe from pandas.
#`

# names= ["Ram", "sita", "anupama", "geetha", "Anvi", "Radhe", "tulasi"]
# san= [95, 80, 96, 94, 70, 80, 86]
# kan = [100, 96, 88, 67, 89, 78, 87]
# hin = [96, 98, 87, 86, 76, 87, 79]
#
# marks= {"s_name": names, "Sanskrit": san, "Kannada": kan, "Hindi":hin}
# marks_sheet= DataFrame(marks)
# print(marks_sheet)



# from pandas import DataFrame
# a=['a','b','c']
# add=[10,20,30]
# sub=[30,40,50]
# dic={'name':a,'adition':add,'subtraction':sub}
# q=DataFrame(dic)
# print(q)

# n=5
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(chr(i+97),end=' ')
#         else:
#             print(' ',end=' ')
#     print()