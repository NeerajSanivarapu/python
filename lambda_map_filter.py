#square of a given number
#by using def keyword
#----------------------------------
# def sq(num):
#     return num**2
# print(sq(5))
#------------------------------------
#by using lambda
#------------------------------------
# a=lambda num:num**2
# print(a(5))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#adding of 2 numbers
##by using def keyword
#----------------------------------
# def add(a,b):
#     return a+b
# print(add(3,4))
##------------------------------------
#by using lambda
#------------------------------------
# a=lambda a,b:a+b
# print(a(3,4))


#write a lambda function to print length of an ineteger
# no=lambda a:len(str(a))
# print(no(10000))

#walf to print number of decimal values present in a float number
# no=lambda a:  len( str(a).split('.')[1])    #2222222
# print(no(10.123456789))


#walf to reverse a string
# a=lambda s:s[::-1]
# print(a('hello'))


# walf to print length of a given string by making square if length is even
#else cube
# a=lambda s: len(s)**2 if len(s)%2==0  else len(s)**3
# print(a('hello'))


#walf to reverse a list
# a=lambda lst:lst[::-1]
# print(a([1,2,3,4,5,6]))


#walf to create a dictionary by taking values from a list key as index value as element
# lst=['😊','😍','👍','🙌','😒','😁','🤣','🤣']
#
# dic=lambda d: dict(enumerate(d))
# print(dic(lst))


#wap to reverse a string if it is having even length else print as it is
# s='hello every one'
# rev=lambda s:s[::-1] if len(s)%2==0 else  s
# print(rev(s))

#walf to print last n no of characters from a collection according to the user input

# a=lambda s,n:s[-n:]
# print(a('hello every one',7))


#map
#wamf to print square of a numbers present in a collection

# a=lambda num:num**2
# lst=[1,2,3,4,5,6,7]
# print(list ( map ( a ,lst) ) )

# print(list(map(lambda num:num**2,[1,2,3,4,5,6,7])))

#wamf to return a length of elements present in a list
# lst=['apple','mango','bannana','neem']
# #o/p==> [5,5,7,4]
# a=lambda a:len(a)
# print(list(map(a,lst)))

#wamf to create a dictionary with key as element value as length of the element
# lst=['apple','mango','bannana','neem','orange','sapota']
# a=lambda a:(a,len(a))    #dict((mango,5))   ---- > {apple:5,mango:5}
# print(dict(map(a,lst)))
#
# print(dict(map(lambda a:(a,len(a)),lst)))


#wamf to create a dictionary from 2 lists
# lst1=['maths','science','java','python','c','mongodb','sql','php']
# lst2=[10,20,30,40,50,60,70,80]
# q=lambda a,b:(a,b)
# print(dict(map(q,lst1,lst2)))
# {'maths': 10, 'science': 20, 'java': 30, 'python': 40, 'c': 50,
# 'mongodb': 60, 'sql': 70, 'php': 80}


#wamf to convert all the elements into upper case
# lst=['apple','neem','tamARind','poTAto','bannANa']
# v=lambda a:a.upper()
# print(list(map(v,lst)))

#['APPLE', 'NEEM', 'TAMARIND', 'POTATO', 'BANNANA']


#wamf to remove space from leading part
#
# lst=['      apple   ','     neem    ','     tamarind    ','     potato  ',
#      '     bannana     ']
#
# v=lambda a:a.lstrip()
# print(list(map(v,lst)))


#wamf to check  elements are starting with vowels or consonents if it is a
#vowel replace with hello else bye

# lst1=['apple','umbrella','python','italy','mongodb','sql','php']

# print(list(map(lambda a: 'hello' if a[0].lower() in 'aeiou' else 'bye',lst1)))


#wamf to check given elemnts are ending with 0 if it is ending with 0 add
# 100 else add 500

# lst=[1000,2345,2100,4321,5430,5678]

# print(list(map(lambda a:a+100 if a%10==0 else a+500,lst)))


#wamf to create a dictionary with length and ending character pair

# lst1=['apple','mango','neem','sapota','tamarind']

# print(dict(map(lambda a:(a[-1],len(a)),lst1)))






#filter
#syntax:
#---------------------


# filter(function,iterable)

#wap to print even numbers present in the given list

# lst=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda lst: lst%2==0,lst)))
# res=[]
#
# for i in lst:
#      if i %2==0:
#           res.append(i)
# print(res)

#wap to print the elements only if the element starts with vowels
# lst=['apple','umbrella','sql','mongodb','python','iran']
# print(list(filter(lambda s:s[0].lower() in 'aeiou',lst)))

#wap to print the values which are divisible by both 5 and 3
# lst=[15,27,45,60,90,9,10]
# print(list(filter(lambda a:a%5==0 and a%3==0,lst)))



#wap to print the elements  which are ending with 00
# lst=[1000,230,3420,4000,5600,7650]
# print(list(filter(lambda a:a%100==00,lst)))

#wap to print the elements which are having odd length and ending with vowel

# lst=['apple','umbrella','orange','tamarind','pottato']
#
# print(list(filter(lambda a:len(a)%2==1 and a[-1].lower() in 'aeiou',lst)))


#wap to return a dictionary woth price more than 100

# name=['apple','umbrella','orange','tamarind','pottato']
# price=[100,200,100,231,123]
# print(dict(filter(lambda a:a[1]>100   ,zip(name,price))))

















