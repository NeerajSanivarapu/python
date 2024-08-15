# if condition:
#     |----------|
#     |   TSB    |
#     |----------|
#  else:
#     |----------|
#     |   FSB    |
#     |----------|

#wap to check whether given number is even or odd
# a=int(input('enter the number'))
# if a%2==0:
#     print('even')
# else:
#     print('odd')

#wap to print hello if the given number is positive else print bye
# a=int(input('enetr the number'))
# if a>0:
#     print('hello')
# else:
#     print('bye')

# wap to convert  given character into upper if it is lower else convert into upper
# ch=input('enter the character')
# if ch.islower():
#     print(ch.upper())
# else:
#     print(ch.lower())

#witout using inbuilt methods

# ch=input('enter the character')
# if ord(ch)>=ord('a') and ord(ch)<=ord('z') :
#     print(chr(ord(ch)-32))
# else:
#     print(chr(ord(ch)+32))

#wap to check whether the given number is divisible by 5 or 8

# a=int(input('enter the number'))
# if a%5==0 or a%8==0:
#     print(f'{a}is divisible by 5 or 8')
# else:
#     print('not divisible')

#wap to check middle letter of a string is upper or not
# s='hello'
# if s[len(s)//2].islower():
#     print(f'{s[len(s)//2]}    it is a lower case letter')
# else:
#     print(f'{s[len(s)//2]}    it is upper case letter')


#wap to check whether the given string is starting with vowel or consonent
# s=input('enter the string')
# if s[0] in 'aeiouAEIOU':
#     print("the name start's with vowel")
# else:
#     print("the name start's with consonent")


#wap to check given year is leap year or not
# year = int(input('enetr the year'))
# if (year %4==0 and year%100!=0 or
#         year %400==0) :
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')

#wap to print fizzbuzz if the given number is divisible by 5 and 3
# else  print fizz if the given nuber is divisible by 5
#else priint buzz if the given number is divisible by 3

# num=int(input('enter your number:'))
# if num%5==0 and num%3==0:
#     print('fizz buzz')
# elif num%5==0:
#     print('fizz')
# elif num%3==0:
#     print('buzz')
# else:
#     print(f'{num} is not divisible by 5 or 3 ')


#wap to return the total amount to be paid by calculating the intreset
# based on type of loan
# [ personal loan :11%,    agriculture loan 5%   ,  car loan 9%]
# print('welcome to e9 batch ')
# loan_amount=int(input('enter loan amount'))
# print('choose one option from below\n'
#       '         1.personal_loan\n'
#       '         2.agriculture_loan\n'
#       '         3.car_loan')
# num=int(input('enter your option:'))   #1
# if num==1:
#     intrest=loan_amount*11//100
#     total_amt=loan_amount+intrest
#     print('='*50)
#     print(f'loan_amount ={loan_amount}')
#     print(f'intrest ={intrest}')
#     print(f'total_amount={total_amt}')
#     print('='*50)
# elif num==2:
#     intrest=loan_amount*5//100
#     total_amt=loan_amount+intrest
#     print('='*50)
#     print(f'loan_amount ={loan_amount}')
#     print(f'intrest ={intrest}')
#     print(f'total_amount={total_amt}')
#     print('='*50)
# elif num==3:
#     intrest=loan_amount*9//100
#     total_amt=loan_amount+intrest
#     print('='*50)
#     print(f'loan_amount ={loan_amount}')
#     print(f'intrest ={intrest}')
#     print(f'total_amount={total_amt}')
#     print('='*50)
# else:
#     print('enter valid number between 1 and 3 only')
#
# print('thank you for using our calculator from e9 batch ')


#WAP TO CHECK WHETHER STUDENT BELONGING TO TESTING OR PYTHON FULL STACK
# OR JAVA FULL STACK

# batch=input('enter your batch code:')   #psp_vada_e9
# if batch[0:3:1].upper()=='PSP':
#     print('python student')
# elif batch[0:3:1].upper()=='JSP':
#     print('java student')
# elif batch[0:3:1].upper()=='QSP':
#     print('testing student')
# else:
#     print('invalid batch code')

#wap to welcome the tourist based on the city he entered in that state language
# ka=['banglore','mangaluru','mysore']
# ap=['tirupathi','vijayawada','visakapatnam']
# tn=['chennai','madurai','coimbatore']
# city=input('enter the city name').lower()
# if city in ka:
#     print('😊ಕರ್ನಾಟಕಕ್ಕೆ ಸ್ವಾಗತ😊')
# elif city in ap:
#     print('😊ఆంధ్ర ప్రదేశ్ కు స్వాగతం😊')
# elif city in tn:
#     print('😊தமிழகத்திற்கு வரவேற்கிறோம்😊')
# else:
#     print('enter city is not present in the list \n'
#           '\t\t\t😊😊sorry.......😊😊')
















