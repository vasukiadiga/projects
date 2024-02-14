import random as r
print('Its a number Guessing game!! \n')
a=r.randint(0,100)
b=int(input('Guess a number Between (0,100):'))
while True:
    if b<a:
        b=int(input('guess a Larger number:'))
    elif b>a:
        b=int(input('guess a Smaller number:'))
    elif a==b:
        print('YOU GUESSED IT RIGHT!! \n YOU WON!!')
        break
    else:
        print('Not a valid Number!!')
        break
