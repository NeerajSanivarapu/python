#exception_handling
#handling the unexpected errors or unwanted errors during exicution  of a program
#it is of 4 types
# 1.general exception
#2.specific exception
#3.generic exception
#4.multiple exception

#types of errors
#NameError
#------------------------------
# dinga=10
# print(dingi)
# --> NameError: name 'dingi' is not defined. Did you mean: 'dinga'?
# when ever the variable name is not declared
#AttributeError
#--------------------------------------
# s='hello'
# print(s.append(10))    #-->AttributeError: 'str' object has no attribute 'append'
# when ever the specified function is not belonging to the datatype
#IndexError
#------------------------------------------------
# lst=[1,2,3,4,5,6]
# print(lst[100])  #--> IndexError: list index out of range
# if the specified index isw not present
#ValueError
#------------------------------------------
# s='hello'
# print(s.index('z'))   #--> ValueError: substring not found
# when ever specified element is not present it raises valueerror

#KeyError
#-------------------------------------
# dic={'a':1,'b':2}
# print(dic['c'])    #-->KeyError: 'c'
# when ever specified key is not present
#IoError
#----------------------------------
# import os
# os.chdir(r'C:\Users\pnsan\Desktop')
# with open('sample.txt','w') as file :
#     file.read()     #io.UnsupportedOperation: not readable
#we will gwt io errors in file handling
#SyntaxError
#----------------------------------
# s='hello every one'
# print(s[::-1:])    #SyntaxError: invalid syntax
# lst=[1,2,3,4,5,6]
# print(lst.count(2,1,2)   #SyntaxError: '(' was never closed
# print('hello')


#-----------------------
#syntax:-
#-----------------------
# try:                  #--> program which is throwing error
#     statement
# except:               #--> exicutes if try block through error
#     statement
# else:                 #   --> executes if try block  doesnot through error
#     statement
# finally:              #--> exicutes mandatory
#     statement

#general exception

# a=10
# b=0
# try:
#     print(a/b)                    #ZeroDivisionError
# except:
#     print('dinga you got error')
# else:
#     print('no error')
# finally:
#     print('exicution done')

# a=10
# try:
#     a[0]                           #TypeError
# except:
#     print('error')
# else:
#     print('no error')
# finally:
#     print('exicution done')


#specific Exception

#syntax:-
#-----------------------
# try:                                    #--> program which is throwing error
#     statement
# except Name_of_the_Error:               #--> exicutes if try block through error
#     statement
# else:                                   #   --> executes if try block  doesnot through error
#     statement
# finally:                                #--> exicutes mandatory
#     statement

# a=10
# b=0
# try:
#     a//b  #ZeroDivisionError
# except TypeError:
#     print('Type error')
# else:
#     print('no error')

# o/p-->ZeroDivisionError: integer division or modulo by zero

# try:
#     a//b  #ZeroDivisionError
# except ZeroDivisionError:
#     print('Zero error')
# else:
#     print('no error')

#o/p--->   Zero error


#GENERIC Exception
#syntax:-
#-----------------------
# try:                                    #--> program which is throwing error
#     statement
# except (error1,error2,......):               #--> exicutes if try block through error
#     statement
# else:                                   #   --> executes if try block  doesnot through error
#     statement
# finally:                                #--> exicutes mandatory
#     statement


# a=10
# try:
#     a[10]    #TypeError
# except(TypeError,NameError,IOError,IndexError) as msg:
#     print(msg)
#'int' object is not subscriptable

# a=10
# try:
#     print(b)   #NameError
# except(TypeError,NameError,IOError,IndexError) as msg:
#     print(msg)
#o/p--> name 'b' is not defined

# a=10
# try:
#     a/0   #ZeroDivisionError
# except(TypeError,NameError,IOError,IndexError) as msg:
#     print(msg)
# '''
# ZeroDivisionError: division by zero
# '''


#multiple Exception

# try:
#     statement
# except exception1:
#     statement
# except exception1:
#     statement
# .
# .
# .
# .
#except exceptionN:
    # statement
# else:
#     statement
# finally:
#     statement

# lst=[1,2,3,4,5]
# try:
#     lst[100]   # indexerror
# except IndexError as msg:
#     print('IndexError:',msg)
# except NameError as msg:
#     print('NameError:',msg)
# except AttributeError as msg:
#     print('AttributeError:',msg)
#o/p--> IndexError: list index out of range

# lst=[1,2,3,4,5]
# try:
#     lst1[0]  # NameError
# except IndexError as msg:
#     print('IndexError:',msg)
# except NameError as msg:
#     print('NameError:',msg)
# except AttributeError as msg:
#     print('AttributeError:',msg)
#o/p-->  NameError: name 'lst1' is not defined

# lst=[1,2,3,4,5]
# try:
#     lst[0]]  #SyntaxError
# except IndexError as msg:
#     print('IndexError:',msg)
# except NameError as msg:
#     print('NameError:',msg)
# except AttributeError as msg:
#     print('AttributeError:',msg)
# '''
# SyntaxError: unmatched ']'
# '''

# #wap to divide 2 numbers if the denominator is 0 replace it with 1
# a=int(input('enter numerator'))
# b=int(input('enter denominator'))
# try:
#     print(a//b)
# except ZeroDivisionError:
#     print(a//1)
# else:
#     print('no error')
# finally:
#     print('exicution completed...')

#wap to print the element present in a specific index if index is not  present
#print last element

# lst=[1,2,3,4,5]
# n=int(input('enter the index value :'))
# try:
#     print(lst[n])
# except:
#     print(lst[-1])

#wap to handle the NameError do deepycopy if the name is not exist
# from copy import deepcopy
# lst=[1,2,[3,4]]
# try:
#     print(lst2)  #nameerror
# except:
#     lst2=deepcopy(lst)
#     print(lst2)


#                                    USER DEFINED EXCEPTION

#raise
# class AgeError(Exception):
#     pass
# age=int(input('enter the age'))
# if age>18:
#     print('eligible')
# else:
#     raise AgeError(f'still you nedd to wait for {18-age} years to become major')




#to modify the inbuilt methods error message

# a='10'
# if a//0:
#     print('correct')
# else:
#  raise AttributeError('dinga error is occured')

#wap to handle the error if the user name is having only alpha numeric values
# and length of the user name has to be 6 character
# if not raise an exception  with modifed message
# user_name=input('enter the user name')
# if user_name.isalnum() and len(user_name)==6:
#     print('correct')
# else:
#     raise TypeError('dinga error you u got')

#create one user defined exception to check whether candidate is cleared all
# the subjectselse raise subjecterror (english,maths,science)  pass marks --->50
# maths=int(input('enter your marks'))
# english=int(input('enter your marks '))
# science=int(input('enter the marks'))
# class SubjectError(Exception):
#     pass
# if maths>50 and english>50 and science>50:
#     print('you cleared all the subjects')
# else:
#     raise SubjectError('you fail in the subjects')
#create a user defined exception
# if the user name is having special characters raise special character error
# if user name not having 8 characters  raise length error
#if the user name is not starting with capital letter raise capital letter error
# class SpecialCharacterError(Exception):
#     pass
# class LengthError(Exception):
#     pass
# class CapitalLetterError(Exception):
#     pass
# name=input('enter your name ')
# if name.isalnum() and len(name)==8 and name[0].isupper():
#     print('correct')
# elif name.isalnum()==False:
#     raise SpecialCharacterError('special character is present')
# elif len(name)<8 or len(name)>8:
#     raise LengthError('lenghth is not matching')
# elif name[0].isupper()==False:
#     raise CapitalLetterError('not starting with capital letter')