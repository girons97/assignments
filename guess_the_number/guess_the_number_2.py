import random
secret_number = random.randint(0,100)

def guess_a_number():
    while True:
        guess = input('Guess a number between 0 and 100: ')

        if type(int(guess)) == int:
            return int(guess)
        elif type(float(guess)) == float:
            print('Please guess an integer')
        else:
            print('Please guess a number')

def is_positive_and_in_range(guess):
    return guess >=0 and guess <= 100

while True:
    guess = guess_a_number()
    if is_positive_and_in_range(guess):
        if guess > secret_number:
            print('Your guess is greater than my secret number')
        elif guess < secret_number:
            print('Your guess is less than my number')
        else:
            print('You are correct!')
            break
    else:
        print('Guess needs to be positive and between 0 and 100')