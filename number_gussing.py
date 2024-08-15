import random
i=1
print('@@@@@@@@@@@@number guessing game designed by e9@@@@@@@@@@@@')
while i <=5:
    n=int(input('enter your number:'))
    guess=random.randint(1,50)
    if n<guess:    #1     5

        print(f'the number  you have gussed is too low.....{guess}')
    elif n>guess:
        print(f'the number  you have gussed is too high.....{guess}')
    else:
        print(f'you got it correctly.....{guess}')
    i+=1
print('########### thank you for playing our game from e9 ####################')