#generator
#--> it is use to generate sequence of values without storing the values
#--> generators are created by using def keyword but instead of return we will use yield
#syntax:
#---------------------------
# def generator_name(arg):
#     #statement
#     yield statement_to_return

#wap to return even numbers from a collection
# lst=[1,2,3,4,5,6,7,8,9]
# def even(a):
#     for i in a:
#         if i%2==0:
#             return i
# print(even(lst))
#o/p-->      2

# def even(a):
#     for i in a:
#         if i%2==0:
#             yield i
# print(list(even(lst)))    # [2,4, 6 ,8]
#

#wap to return square and cube of a given number
# n=5
# def sq_cu(n):
#     return n**2
#     return n**3
# print(sq_cu(n))     #o/p-->25

# def sq_cu(a):
#     yield a**3
#     yield a**2
# print(list(sq_cu(5)))     #o/p-->[125,25]

#wap to return 1 to 100 even numbers

# def numbers():
#     for i in range(1,101):
#         if i %2==0:
#             yield i
# print(list(numbers()))

#wap to return elements which are starting with vowels
# lst=['Instagram','Apple','Facebook','whatsapp','Twitter','umbrella']
# def vowels(a):
#     for i in a:
#         if i[0].lower() in 'aeiou':
#             yield i
# print(list(vowels(lst)))     #o/p-->  ['Instagram', 'Apple', 'umbrella']

#wap to return a list with a tuples of word and reversed word pair
# lst=['Instagram','Apple','Facebook','whatsapp','Twitter','umbrella']

# def sample(a):
#     for i in a:
#         yield (i,i[::-1])
# print(list(sample(lst)))

#o/p-->   [('Instagram', 'margatsnI'), ('Apple', 'elppA'),
# ('Facebook', 'koobecaF'), ('whatsapp', 'ppastahw'), ('Twitter', 'rettiwT'),
# ('umbrella', 'allerbmu')]

#wap to return a list with a tuples of word and length pair if it is
# having even length else word and index pair
lst=['Instagram','Apple','Facebook','whatsapp','Twitter','umbrella']
# def demo(a):
#     for i,j in enumerate(a):
#         if len(j)%2==0:
#             yield (j,len(j))
#         else:
#             yield(j,i)
# print(list(demo(lst)))

#o/p-->[('Instagram', 0), ('Apple', 1), ('Facebook', 8), ('whatsapp', 8),
# ('Twitter', 4), ('umbrella', 8)]


#generator expression



#syntax:
#--------------------------------------

# if no condition:-   (expression for variable_name in collection)
# only if condition :-  (expression for variable_name in collection if condition)
#both if and else conditions:- (expression if condition else  expression for variable_name in collection)

# wage to return even numbers present in a collection
# lst=[1,2,3,4,5,6,7,8,9]
# # (exp for i in lst   if condition)
# a=(i for i in lst if i %2==0)
# print(list(a))

#wage to return sqaure if it is even else odd
# lst=[1,2,3,4,5,6,7,8,9]
# a=(i**2 if i%2==0 else i**3 for i in lst)
# print(list(a))
#o/p-->[1, 4, 27, 16, 125, 36, 343, 64, 729]


#wage to retun a list of tuples with value ,square and cube of the value

# lst=[1,2,3,4,5,6,7]
# a=((i,i**2,i**3) for i in lst)
# print(list(a))
#[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343)]


# #wage to  return hello if the given string middle character is vowel else bye
# s='hello'
#
# a=('hello' if s[len(s)//2].lower() in 'aeiou' else 'bye' )
# print(str(a))






