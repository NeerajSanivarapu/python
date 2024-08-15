#wap to find factorial of a given number
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#             #   5 * fact(4)
#             #5*4*fact (3)
#             #5*4*3*fact(2)
#             #5*4*3*2*fact(1)
#             #5*4 * 3*2*1*fact(0)
#             #5 * 4 *3 *2  *1 *1
#         #return 120
# print(fact(5))


#wap to find sum of the given number
#i/p:-->12345  --> o/p:-->15

# def sum_of_digits(n):  #0
#     if n==0:
#         return 0
#     else:
#         return n%10 +sum_of_digits(n//10)
#                 #5  + sum_if_digits(1234)
#                 #5+4+sum_of_digits(123)
#                 #5 +4 +3 +sum_of_digits(12)
#                 #5 +4 + 3+2 +sum_of_digits(1)
#                 #5+4+3+2+1+sum_of_digits(0)
#           #return       #5 + 4+ 3 +2 +1 +0
#
# print(sum_of_digits(12345))

#wap to reverse a string by using recursion

# def reverse_string(s):   # hello  ---> olleh
#     if len(s)==0:
#         return ''
#     else:
#         return s[-1]+reverse_string(s[:-1])     # s[0:-1:1]
#               #o  +reverse_string(hell)
#               #o+l +reverse_string(hel)
#               # o+l+l+reverse_string(he)
#                 #o + l + l+e +reverse_string(h)
#                 #o + l + l + e + h +reverse_string ('')
#                 #o + l + l + e  + h +'' ========> olleh
# print(reverse_string('hello'))


# palindrome or not

#malayalam
# def palindrome(s):
#     if len(s)<=1:
#         return True
#     else:
#         return s[0]==s[-1] and palindrome(s[1:-1])
#             #m==m      and   palindrome(alayala)
#             #m==m and a== a and palindrome(layal)
#             #m==m  and a==a and l==l and palindrome(aya)
#             #  #w==m  and a==a and l==l and a==a and palindrome(y)
#             #      T       T       T        T        T
# print(palindrome('malayalam'))
# print(palindrome('python'))



#wap to find the power of the given number
# def power(x,y):
#     if y==0:
#         return 1
#     else:
#         return x*power(x,y-1)
#               # 2 * power(2,3-1)
#               #2*2*power(2,2-1)
#               #2 *2 * 2 * power(2,1-1)
                #2*  2 * 2 * 1===> 8
# print(power(2,3))

#wap to count how many vowels are present in a given string
# def count_vowel(s):
#     if len(s)==0:
#         return 0
#     else:
#         return (1 if s[0].lower() in 'aeiou' else 0)+count_vowel(s[1:])
#             # 0     +   count_vowel(inga)
#             # 0   +   1  +count_vowels(nga)
#             #0 + 1 + 0+count_vowels(ga)
#             #0 + 1 + 0 + 0 + count_vowels(a)
#             # 0 + 1+ 0 + 0 + 1 + count('')
# print(count_vowel(input('enter the value :')))



#wap to reverse each word in a given string
# hello python=====>     olleh nohtyp

# def rev(s):
#     #hello python
#     words=s.split()
#     return words[0][::-1]+' ' +words[1][::-1]
# print(rev('hello python'))













