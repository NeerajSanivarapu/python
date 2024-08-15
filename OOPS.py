# class Demo:
#     a=10
#     b=20
#     c=30
# d1=Demo()
# d2=Demo()
# d1.a=100
# d2.b=200
# Demo.c=300
#
# Demo.a=200
# print(Demo.a)
# print(d1.a)
# print(d2.a)


# class Sample:
#     def add(a,b):
#         print(a+b)
# s1=Sample()
# s1.add(10,20)

# class Addition:
#     def add(self,a,b):
#        print(a+b)
#
# a1=Addition()
# a1.add(10,20)    #o/p===>   30
# a2=Addition()
# a2.add(30,40)      #o/p ==> 70

# class Bank:
#     b_name='SBI'
#     address='chennai'
#     ifsccode='SBI0101001'
#     def __init__(self,c_name,phno,acno):
#         self.customer_name=c_name
#         self.phone_number=phno
#         self.account_no=acno
# b1=Bank('dinga',12345,'a1b2c3')
# print(b1.b_name)    #icici
# print(b1.address)
# print(b1.ifsccode)
# print('='*20)
# print(b1.customer_name)
# print(b1.phone_number)
# print(b1.account_no)
# print('*'*20)
# b2=Bank('dingi',1345,'d5e7f7')
# print(b2.b_name)     #sbi
# print(b2.address)
# print(b2.ifsccode)
# print('='*20)
# print(b2.customer_name)
# print(b2.phone_number)
# print(b2.account_no)

# o/p====>
# SBI
# chennai
# SBI0101001
# ====================
# dinga
# 12345
# a1b2c3
# ********************
# SBI
# chennai
# SBI0101001
# ====================
# dingi
# 1345
# d5e7f7



# class Bank:
#     b_name='SBI'
#     address='chennai'
#     ifsccode='SBI0101001'
#     def __init__(self,c_name,phno,acno):
#         self.customer_name=c_name
#         self.phone_number=phno
#         self.account_no=acno
#     @classmethod
#     def change_name(cls):
#         cls.b_name='ICICI'
#         print('name changed sucesfully......')
# b1=Bank('dinga',1234,1234567878)
# b2=Bank('dingi',5678,987654321)
# print(b1.b_name)
# print(b2.b_name)
# b1.change_name()
# print('-------------------after changing------------------')
# print(b1.b_name)
# print(b2.b_name)
# print(Bank.b_name)

# SBI
# SBI
# name changed sucesfully......
# -------------------after changing------------------
# ICICI
# ICICI
# ICICI



##############      INHERITANCE    #######################
# class w_v1:      #super class
#     def chat(self):
#         print('chatting')
#     def status(self):
#         print('status ')
#
# o1=w_v1()
# class w_v2(w_v1):     #sub class
#     def loc(self):
#         print('location')
#     #loc   chat   #status
# v1=w_v2()
# v1.loc()
# v1.chat()
# v1.status()

# ____________ creating 2 diffent files ____________
# from OOPS import w_v1

# class w_v2(w_v1):
#     def loc(self):
#         print('location')
# v1=w_v2()
# v1.loc()
# v1.chat()
# v1.status()




#multi level
# class w_v0:
#     def gifs(self):
#         print('gifs')
# class w_v1(w_v0):  #gifs
#     def chat(self):
#         print('chatting')
#     def status(self):
#         print('status ')
# class w_v2(w_v1):
#     def loc(self):
#         print('location')
# #gifs chat status    loc
# class w_v3(w_v2):
#     def payment(self):
#         print('payment')
# w1=w_v3()
# w1.gifs()
# w1.chat()
# w1.status()
# w1.loc()
# w1.payment()

# intern


#hirarchical inheritance

# class Facebook:      #super class
#     def aifilter(self):
#         print('ai')
# class Whatsapp(Facebook):    #1 sub class
#     #aifilter
#     def story(self):
#         print('story')
# class Insta(Facebook):    #2nd sub class
#     def filter(self):
#         print('filter')
#
# f1=Facebook()
# f1.aifilter()
#
# w1=Whatsapp()
# w1.aifilter()
# w1.story()
#
# i1=Insta()
# i1.filter()
# i1.aifilter()




#multiple
#
# class parent1:      #super class
#     def chat(self):
#         print('chatting')
# class parent2:      #super class
#     def story(self):
#         print('story')
# class parent3:
#     def filter(self):
#         print('filter')
# class child(parent1,parent2,parent3):    #sub class
#     def ai(self):
#         print('ai features are present ')
#
#     #chat   #story
# c1=child()
# c1.filter()
# c1.ai()
# c1.story()
# c1.chat()

#assignment
# ( for inheritance concepts 1 program for each type) and hybrid inheritance

#hybrid inheritance
# it is a combination of multiple and hirrachical inheritance
# class Animal:   #super class
#     def sound(self):
#         print('animal sounds')
# class lion(Animal):     #subclass
#     def hunting(self):
#         print('hunting')
#     #sound
# class Tiger(Animal):    #sub class
#     def running(self):
#         print('running')
#     #sound
# class Liger(lion,Tiger): #grand child
#     def height(self):
#         print('height')
#     #sound hunting running
# l1=Liger()
# l1.hunting()
# l1.height()
# l1.sound()
# l1.running()





#method overriding


# class whatsapp_v1:
#     def chat(self):
#         print('chatting ,payment')    #30000
# # location
# #contacts
# class whatsapp_v2(whatsapp_v1):
#     # chat
#     def chat(self):   #  lcation contacts
#         print('location,contacts')
#         super().chat()   #chatting payment
#
# w2=whatsapp_v2()
# w2.chat()






#poymorphisam

# s='hello'
# print(type(len(s)))    #string function  length
# print(len([1,2,3,4,5]))      # list function
# print(len({1:1,2:2,3:3}))    #dictionary function
# # print(len(100))    # error

#by using operators
# (+ ,- , *)
# addition (+)
# print(10+5)


#concatination (+)
# print('hello'+' hi')
#
# lst=[1,2,3,4]
# lst2=[5,6,7,8]
# print(lst+lst2)
#
# s=(1,2,3,4)
# s1=(5,4,3,2)
# print(s+s1)

#sub (-)
# print(10-2)
# lst={1,2,3,4,5,6,7}
# lst2={2,3,4,5,6,7,8}
# print(lst-lst2)


#multi( *)
# print(10*2)
#
# print('hi'*30)
# print([1,2,3]*10)

#
# class student:
#     def pay_bills(self):
#         print('loan app ,betting')
# class employee:
#     def pay_bills(self):
#         print('credit card ,tax')
# class manager:
#     a=10
#     def pay_bills(self):
#         global a
#
# s1=student()
# e1=employee()
# m1=manager()
# e1.pay_bills()    # employeee     # credit card ,tax
# s1.pay_bills()      #student     # loan app ,betting
# m1.pay_bills()       #manager     # office rent ,salaries



#BY USING INHERITANCE
#----------------------------------------
# class Animal:
#     def sound(self):
#         print('Animal sound')
# class cat(Animal):
#     #sound
#     def sound(self):
#         print('cat sound')
# class Dog(Animal):
#     def sound(self):
#         print('Dog sound')
# class rat(Animal):
#     def sound(self):
#         print('rat sound')
# def mediator(obj):     #r1
#     obj.sound()          #r1.sound()
# c1=cat()
# d1=Dog()
# r1=rat()
# c1.sound()
# d1.sound()
# r1.sound()
# # mediator(c1)
# # mediator(d1)
# # mediator(r1)



# ABSTRACTION
#---------------------------------------------------------------
# from abc import ABC,abstractmethod
# class Demo(ABC):
#     @abstractmethod
#     def story(self):
#         pass
#     @abstractmethod
#     def post(self):
#         pass
#     @abstractmethod
#     def reels(self):
#         pass
#     @abstractmethod
#     def filters(self):
#         pass
#     def chat(self):    # concrete method
#         print('chat code')
#
# class Instagram(Demo):
#     def story(self):
#         print('story code')
#     def reels(self):
#         print('reels  code')
#     def filters(self):
#         print('filters code')
#     def post(self):
#         print('post code')
# i1=Instagram()
# i1.post()
# i1.filters()
# i1.reels()
# i1.chat()
# i1.story()



#ENCAPSULATION
#-------------------------------------------

# class Sample:
#   def __init__(self,name,age):
#       self.name=name
#       self.age=age
# s1=Sample('dinga',23)
# print(s1.name)
# print(s1.age)

# class Demo(Sample):
#     def add(self):
#         print(Sample.name)
# d1=Demo()
# d1.add()


# class Demo:
#     def __init__(self,name ,age):
#         self._name=name     #ox11._name=='dinga'    #ox12._name==>dingi
#         self._age=age    #ox11._age  ==23           #ox12._age ==> 22
#
# dinga=Demo('dinga',23)   #ox11
# dingi=Demo('dingi',22)    #ox12
#
# print(dinga._name)  #ox11._name
# print(dingi._age)

'''
we can access protected variables outside the class but according to the convension
we should not access them outside the class
'''



# class Demo:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
# d1=Demo('dinga',23)
# d2=Demo('dingi',22)
# print(d1.__age)     #AttributeError: 'Demo' object has no attribute '__age'
# print(d2.__name)    #AttributeError: 'Demo' object has no attribute '__name'
#


#getters and setters
#getter we can get the value
#setter we can set the value

#
# dic={'dinga':1234,'dingi':4561}
# class person:
#     def __init__(self,name ,age):
#         self.__name=name
#         self.__age=age
#     def get_details(self,a):   #ox11
#         if a==dic[self.__name]:
#             print(self.__name,self.__age)
#         else:
#             print('incorrect password...')
#     def set_details(self,age,b):
#         if b==dic[self.__name]:
#             self.__age=age
#         else:
#             print('invalid password...')
# p1=person('dinga',23)
# p2=person('dingi',22)
# p2.get_details(4561)
# p1.get_details(1234)
# print('='*100)
#
# p1.set_details(24,1234)
# p2.set_details(23,4561)
# p1.get_details(1234)
# p2.get_details(4561)
#
#
# # dingi 22
# # dinga 23
# # ====================================================================================================
# # dinga 24
# # dingi 23
# dic={'dinga':1234,'dingi':4561}
# class person:
#     def __init__(self,name ,age):
#         self.__name=name
#         self.__age=age
#     def get_details(self,a):   #ox11
#         if a==dic[self.__name]:
#             print(self.__name,self.__age)
#         else:
#             print('incorrect password...')
#     def set_details(self,age,b):
#         if b==dic[self.__name]:
#             self.__age=age
#         else:
#             print('invalid password...')
# p1=person('dinga',23)
# p2=person('dingi',22)
# p2.get_details(4561)
# p1.get_details(1234)
# print('='*100)
#
# p1.set_details(24,1234)
# p2.set_details(23,4561)
# p1.get_details(1234)
# p2.get_details(4561)
#
#
# # dingi 22
# # dinga 23
# # ====================================================================================================
# # dinga 24
# # dingi 23





#
# #      @property
#
# # @ property       --> for the getter function
# # @function_name.setter     --> used to assign the setter method
# #@function_name.deleter  --> used to delete the members
#
#
# class sample:
#     def __init__(self,name):
#         self.__name=name
#     # def get_details(self):
#     #     print(self.__name)
#      @property
#     def ge(self):
#         return self.__name
#     @set_details.setter
#     def set_details(self,name):
#         self.__name=name
# s1=sample('dinga')
# # print(s1.get_details())
# # print(s1.ge)































