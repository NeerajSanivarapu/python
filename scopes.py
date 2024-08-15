#global scope
#----------------------------------------------------------
# a=10
# def add():
#     global a
#     a=11
#     print('during function exicution ',a)
# print('before exicution of the function ',a)
# add()
# print('after exicution of function ',a)



#o/p-->
# before exicution of the function  10
# during function exicution  11
# after exicution of function  11



# local scope

# def add():
#     a=100   #---> local variable
#     print(a)   #100

# print(a)   #error
# def outer():
#     a=10   #local variable
#     print('before modifying',a)
#     def inner():
#         nonlocal a   #non local variable
#         a+=1
#         print('during modifying',a)
#     inner()
#     print('after modifying',a)
# outer()

#
# outer=1000 -------------------------------------------->global variable
# def first_fun():
#     global outer
#     outer=12
#     print('during first function',outer)
#     inner=10  -----------------------------------------> local variable
#     print('before exicution ',inner)
#     def inner_func():
#         global outer
#         outer=100
#         print('inner func output of a ',outer)
#         nonlocal inner -------------------------------> non local variable
#         print('non local variable',inner**3)
#     inner_func()
# print('before exicution',outer)   #1000
# first_fun()     # 12       #100
# print('after exicution',outer)    #100

# before exicution 1000
# during first function 12
# before exicution  10
# inner func output of a  100
# non local variable 1000
# after exicution 100
print('hello','hi',sep='@',end=' ')
print('good')



