#split()
#--> it is used to split the given string based on max_splits
#by default it will split the spaces
#syntax:
#--------------
##string.split('character',max_splits)
##s='hello every one'
##print(s.split())
##s='malayalam'
##print(s.split('a'))
###[m,l,y,l ,m]
##print(s.split('a',2))
##print(s.split('a',100))
##print(s.split('z'))

#strip()
#-----------------
        #h   e     l     l       o        
# it is used to remove specified element from both leading and tailing part
# by default it removes space
#syntax
#--------------------
##string.strip('element')
####s='           hello           '
####print(s)
####print(s.strip())
##s='@@@@hello@@@@'
##print(s.strip('@'))

##s='@@#@@he@llo@@@@'
##print(s.strip('@'))

# isupper()
#it return True /False
# if the given string is having completely uppercase characters
#it won't accept any argument
#syntax :
#-----------------
# string.isupper()
#s='HELLO'
#print(s.isupper())    #True
#s='HElLO'
##print(s.isupper())

##s='HELLO1'
##print(s.isupper())
##s='HELL@123'
##print(s.isupper()) 
##s='123456'
##print(s.isupper()) 


#islower()
#------------------------
#it return True /False
# if the given string is having completely lowercase characters
#it won't accept any argument
#syntax :
#-----------------
# string.islower()
#s='hello'
##print(s.islower())
##s='hEllo'
##print(s.islower())
##s='1hello'
##print(s.islower())
##s='@pple'
##print(s.islower())


#isalpha()
#it returns true if the given string is having completely alphabets
#it wont accept any argument
# syntax :
#-----------------------
##string.isalpha()
#s='heLLo'
##print(s.isalpha())
#s='hello1'
##print(s.isalpha())
##s='@pple'
##print(s.isalpha())
##s='hello every one'
##print(s[::2].upper()[::-1].split('O'))
#hloeeyoe.upper()----->HLOEEYOE ---> E|YEE|LH----> [E,YEE,LH]

#isdigit()
# it return true if the string contains only numbers
#it wont accept any argument
#syntax :
#------------------
##string.isdigit()

##s='12345'   
##print(s.isdigit())

##s='123G'
##print(s.isdigit())

#isalnum()
#--------------------------
#it return True if the given string is having completely alphabets
#   or
#it return True if the given string is having completely numbers
# or 
#it return True if the given string is having combination of alphabets and numbers
##s='hello'
##print(s.isalnum())
##s='123'
##print(s.isalnum())
##s='a1h2e3'
##print(s.isalnum())
##s='@'
##print(s.isalnum())

#isspace()
#------------------------
#it return if the given string is having completely space
# it wont accept any argument
#syntax:
#----------
#string.isspace()
##s='             '
##print(s.isspace())
##s='       h        '
##print(s.isspace())
#----------------------------------
#indexing and slicing
#----------------------------------
#upper lower swapcase capitalize title  # --> 
#index find  split  strip,count     
#isupper islower isalpha isdigit isalnum isspace  isidentifer()


# LIST
#-----------------------------------------
# it is a collection of homogeneous and hetrogeneous type of data
# boundaries of list are []
# list is a mutable datatype
#list allows duplicates  [1,2,3,1,2,4,5]
#list is a ordered datatype [1,2,3]     -----> 1   2     3
# list supports indexing and slicing
#default value of list is []
##[1,2,3,4,5]
#    0 1 2 3 4 
# indexing :---->>> ls[index]
#slicing     :------>>>    ls[si:ei:sv]
##print(ls[2])
##print(ls[1:4:2])   #2 4

##lst=['apple','bannana','mango',[1,2,3,4,[5,6]]]
##print(lst[0])   #apple
##print(lst[1].count('n'))
##print(lst[2][3])
##print(lst[2][3])     #'mango'[3] ---'g'

##lst
##lst=['apple', 'bannana', 'mango', [1, 2, 3, 4, [5, 6,'tamarind']]]
##lst[3]
##[1, 2, 3, 4, [5, 6]]
##lst[3][4]
##[5, 6]
##lst[3][4][1]
##6

#D
##print(lst[3][4][2][-1].upper())






































