
##############################   REG_EX ################################
#1.   '.'--> it will match with n no of characters except next line
# import re
# s='helloworld\nddddd'
# res=re.findall('.',s)
# # print(res)          ['h','e''l'........]
# findall==> it returns a list consists of all the matched elements

# 2.   '\.' --> it will match with dot

# import re
# s='hello.w...\n\n..........orld.hi'
# res=re.findall('\.',s)
# print(res)

# 3.    "\\"  --> it is use to match with the forward slash
# import re
# s='hello//fffffff'
# res=re.findall("\\",s)
# print(res)

# 4. [abcd]---> usr to match either a or b or c or d

# import re
# s='hello ram how are you'
# #aeiou
# res=re.findall("[aeiou]",s)
# print(res)
#[a-z]
# s='HeLlO 12121 EvErY One'
# res=re.findall("[a-z]",s)
# print(res)
# s='hell @ World  12321211 EQR swa'

# #[a-zA-z]
# res=re.findall("[a-zA-Z]",s)
# print(res)
# s='hello 123 @@@@@!!!!!!     WORld'
# #[a-zA-Z0-9]
# res=re.findall("[a-zA-Z0-9]",s)
# print(res)
# s='hello@@@123'

# [^a-z]--> it rejects a-z characters
#[^0-9]
# res=re.findall("[^a-z]",s)
# print(res)
# res=re.findall("[^0-9]",s)
# print(res)

# res=re.findall("[^a-zA-Z0-9]",s)
# print(res)

# match all the characters ALONG WITH UNDER SCORE
#DINGA_ 123 DINGI
# import re
# s="DINGA_ 123 DINGi"
# res=re.findall("[a-zA-Z_]",s)
# print(res)

#    \w--> it will match with alphabets numbers and _    [a-zA_Z0-9_]
# res=re.findall("\w",s)
# print(res)


#    \W --> it is use to exculde the aplabets number and _ [^a-zA_Z0-9_]
import re
# s='DINGa 123 @@@@ ____ $$ %%%% dingi'
# res=re.findall("\W",s)
# print(res)
# [' ', ' ', '@', '@', '@', '@', ' ', ' ', '$', '$', ' ', '%', '%', '%', '%', ' ']


#     \d --> used to match with digits     [0-9]
# s='DINGa 123 @@@@ ____ $$ %%%% dingi'
# res=re.findall("\d",s)
# print(res)
 #['1', '2', '3']

# res=re.findall("\D",s)    [^0-9]
# print(res)
# ['D', 'I', 'N', 'G', 'a', ' ', ' ', '@', '@', '@', '@', '
# ', '_', '_', '_', '_', ' ', '$', '$', ' ', '%', '%', '%', '%',
# ' ', 'd', 'i', 'n', 'g', 'i']




#\w
#\W
#\d
#\D
# [a-z]
# [A-Z]
# [a-zA-Z0-9]
# [^a-z]
# [^a-zA-Z0-9]
#[^0-9]

# r'^h'
# r='h$'
#
# ^-- starting
# $ -it is ending


# wap to print only spaces
# s='hello every one'
#wap to print only consonents
#wap to print only alphanumeric values
#wap to print special characters with under score also
#wap to print  the characters except 0-5 numbers
#wap to print the characters except new line
#wap  to print raj from the given string
# s='hello raj rajan'
#  [raj, raj]
# res=re.findall('raj',s)
# print(res)
#wap to print 'o' from the given string
# s='hello every one good after noon'
#wap to print 'oo'  from the given string
# s='hello every one good after noon'



# wap to find whether student is belong to pyspiders
import re
# a=input('enter your branch:')   #pyspiderspy
# b=re.findall(r'^py',a)    #[]--> False
# # # if b!=[]:
# # # if b:   #false
# if b:      #if True:
#     print('you are a python student')
# else:
#     print('you are not a python student')


#wap to check given  word is starting with h print string as
# it is else print reverse of the string
# s='hello world'
# a=re.findall(r'^h',s)
# print(a)
# if a!=[]:   #['h']
#     print(s)
# else:
#     print(s[::-1])


#wap to check given word is ending with   d
# s='hello world!'
#
# if re.findall(r'd$',s):    #[]-->False
#     print(s)
# else:
#     print('nothing')

#wap to check given student or belonging to qspiders ,jspiders,prospiders,pyspiders
#using reg_ex

# s='gspiders'
#
# if re.findall(r'^py',s):
#     print('python student')
# elif re.findall(r'^q',s):
#     print('testing student')
# elif re.findall(r'^j',s):
#     print('java student')
# elif re.findall(r'^pro',s):
#     print('pro spiders student')
# else:
#     print('not belongs to any spiders')


# wap to check given name is starting with vowel or not
# s='apple'
# if re.findall(r'^[aeiouAEIOU]',s):
#     print(s)

#wap to check given name is ending with vowel

# s='apple'
# if re.findall(r'[aeiouAEIOU]$',s):
#     print(s)

#wap to check given name is starting with h and ending with d
# s='hello world'
# a=re.findall(r'^h.*d$',s)
# print(a)
# # ['hello world']
# if a!=[]:   #[]  != []
#     print('hello')
# else:
#     print('else')






























