
# list comprehension

#no condition
# [exp for i in list]


#only if block is using
#[exp for i in list if condition]

#both if and else are using
#[exp if condition else exp for i in lst]


#wap to create a list  by making sqaures of the elements present in the existing list

# lst=[1,2,3,4,5,6,7,8,9]
# res=[]
# for i in lst:
#     res.append(i**2)
# print(res)

#comprehension
# lst=[1,2,3,4,5,6,7,8,9]
# res=[i**2 for i in lst]
# print(res)


#wap to create a list by making square of the elements present in existing list
# if element is even
# lst=[1,2,3,4,5,6,7,8,9]
# res =[]
# for i in lst:
#     if i %2==0:
#         res.append(i**2)
# print(res)

#comprehension
# res=[i**2 for i  in lst if i%2==0]
# print(res)

#wap to create a list if the elements present in the list is divisible by 5
# lst=[10,15,25,32,21,18]
# res=[]
# for i in lst:
#     if i %5==0:
#         res.append(i)
# print(res)


#comprehension
# res=[i for i in lst if i%5==0]
# print(res)

#wap to create a list  by making sqaures of elements present in
# the list if it is even else cube
# lst=[1,2,3,4,5,6,7,8,9,10]
# res=[i**2 if i %2==0 else i**3 for i in lst]
# print(res)
#[1, 4, 27, 16, 125, 36, 343, 64, 729, 100]

#wap to create a list by adding 100 if the element is ending  with 0 else add 1000
# lst=[10,25,21,34,66,40,500]
#
# res=[i+100 if i%10==0  else i+1000 for i  in lst  ]
# print(res)
# [110, 1025, 1021, 1034, 1066, 140, 600]



#wap to create a list by raising the element to its index power
# lst=[1,2,3,4,5,6,7,8,9]
# res=[]
# for index,value in enumerate(lst):
#    res.append( value**index)
# print(res)

#[1, 2, 9, 64, 625, 7776, 117649, 2097152, 43046721]


# res=[value**index for index,value in enumerate(lst)]
# print(res)


#wap to return a list  if the words present in the list is having
# even length reverse the word and add else print lengtgh of the word
# lst=['dinga','ram','ravi','dingi','qspiders','pyspiders','jspiders','prospiders','gspiders']
# res=[]
# for i in lst:
#     if len(i)%2==0:
#         res.append(i[::-1])
#     else:
#         res.append(len(i))
# print(res)


#comprehension
# res=[i[::-1]if len(i)%2==0 else len(i) for i in lst ]
#
# print(res)
#o/p==> [5, 3, 'ivar', 5, 'sredipsq', 9, 'sredipsj', 'sredipsorp', 'sredipsg']


###########################      ASSIGNMENT ###########################################################
#1.wap to create a list by taking the keys from a dictionary if the values are even

# dic={'tomato':23,'grapes':22,'orange':18,'apple':55,'neem':123456}
# res=[]
# for i in dic:        #tomato
#     if dic[i]%2==0:
#         res.append(i)
# print(res)

# res=[i for i in dic if dic[i]%2==0]
# print(res)
# o/p==>  ['grapes','orange','neem']

#2.wap to create a list with keys value from a dictionary if the values are even

# dic={'tomato':23,'grapes':22,'orange':18,'apple':55,'neem':123456}
# res=[]
# for i in dic:        #tomato
#     if dic[i]%2==0:
#         res.append((i,dic[i]))
# print(res)

# res=[(i,dic[i]) for i in dic if dic[i]%2==0]
# print(res)
#o/p==> [('grapes',22),('orange',18),('neem',123456)]

#3.wap to create a list if it is only vowel
# lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
# 'v','w','x','y','z']
# res=[]
# for i in lst:
#     if i.lower() in 'aeiou':
#             res.append(i)
# print(res)
#
# a=[i for i in lst if i.lower() in 'aeiou']
# print(a)

#4. wap to create a  list only for fruits
# lst=['rose flower','grapes fruit','apple fruit','orange fruit','neem plant','tomato vegetable',
#      'onion vegetable','papaya fruit']
# res=[]
# for i in lst:      # rose flower
#      a=i.split()
#      if a[1] =='fruit':
#           res.append(a[0])
# print(res)
#
# a=[i.split()[0] for i in lst if i.split()[1]=='fruit']
# print(a)






#set comprehension

#wasc by taking elements present in a list  square and add

# lst=[1,2,3,4,5,6,7,8,3,4,2,3,4,2]
# s=set()
# for i in lst:
#      s.add(i**2)
# print(s)
#--------------------
#comprehension      |
#--------------------
# s={i**2 for i in lst }
# print(s)

#o/p==>{64, 1, 4, 36, 9, 16, 49, 25}

#wasc to  if the elements are not starting with vowels and upper case

# lst=['Google','Apple','facebook','twitter','Instagram','snapchart','gpay']
# #o/p==>  {facebook,snapchart,twitter gpay}
# s=set()
# for i in lst:
#      if i[0].lower() not in 'aeiou' and i[0].islower():
#           s.add(i)
# print(s)


# s={i for i  in lst if i[0].lower() not in 'aeiou' and i[0].islower()}
# print(s)



#wasc  by taking input from a list if the given number is divisible by 5 add
# 10% hike  else add 5% hike
# lst=[100,232,343,452,655,761,890]
# s=set()
# for i in lst:
#      if i%5==0:
#           s.add(i+i*10//100)
#      else:
#           s.add(i+i*5//100)
# print(s)


# s={ i+i*10//100 if i %5==0 else i+i*5//100 for i in lst }
# print(s)

#o/p==>{360, 110, 720, 243, 979, 474, 799}

#dictionary


#wadc from a list key as value and element as square if it is even else  cube
# lst=[1,2,3,4,5,6,7,8,9,10]
# dic={}
# for i in lst:
#      if i%2==0:
#           dic[i]=i**2
#      else:
#           dic[i]=i**3
# print(dic)
#
# {1: 1, 2: 4, 3: 27, 4: 16, 5: 125, 6: 36, 7: 343, 8: 64, 9: 729, 10: 100}
# a={i:i**2if i%2==0 else i**3 for i in lst}
# print(a)

#wadc to print a city and population pair
# city =['banglore','chennai','mumbai','hyderabad','vizag','coimbatore']
# population=[1000000,2000000,5000000,25000000,100000,213456]
# dic={}
# for i,j in zip(city,population):
#      #i==>city     #j==> population
#      dic[i]=j
# print(dic)
#
#
# a={i:j for i,j in zip(city,population)}
# print(a)


#wadc if the word is starting with vowel add word and reversed word pair
# else word and length pair
# lst=['apple','grapes','bannana','orange','neem','sun flower']
# dic={}
# for i in lst:
#     if i[0].lower() in 'aeiou':
#         dic[i]=i[::-1]
#     else:
#         dic[i]=len(i)
# print(dic)
# dic={i:i[::-1] if i [0].lower() in 'aeiou' else len(i) for i in lst}
# print(dic)
#o/p==>{'apple': 'elppa', 'grapes': 6, 'bannana': 7, 'orange': 'egnaro',
# 'neem': 4, 'sun flower': 10}





























 # WAP to traverse and print all the elements with sub heading as
# key name.
d = {"Fruits": ["Mango", "Apple", "Kivi", "Grapes", "Banana"],
     "Vegitables": ["Tomato", "Potato", "Onion", "Spinach", "Beans"],
     "Plants": ["Neem", "Money plant", "alovera plant", "Rose plant"],
     "Trees": ["Banian tree", "Coconut tree", "sandal wood tree"]}
count=1
for i in d:
    print(f'{count}. {i}')
    count+=1
    alphabet='a'
    for j in d[i]:   #mango
       print(f'       {alphabet}.{j}')
       alphabet=chr(ord(alphabet)+1)

'''
1. Fruits
       a.Mango
       b.Apple
       c.Kivi
       d.Grapes
       e.Banana
2. Vegitables
       a.Tomato
       b.Potato
       c.Onion
       d.Spinach
       e.Beans
3. Plants
       a.Neem
       b.Money plant
       c.alovera plant
       d.Rose plant
4. Trees
       a.Banian tree
       b.Coconut tree
       c.sandal wood tree

'''







