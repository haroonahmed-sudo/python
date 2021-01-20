import random

print("Number Guessing Game, You Have 5 Chance's")
count = 0



while True:
    rand = random.randint(1, 9)
    count += 1

    if count == 6:
        print('Finished')
        break
    else:
        number = int(input('Enter Any Number Between 1 To 9: '))
        if(number >= 1 and number <=9):
            
            print('Your Number ', number)
            print('Random Number ',rand)
            if(rand == number):
                print('Congrats')
                break
            else:
                print('Try Again')
        else:
            print('You Should Choose Numbers between 1 To 9')
            break



