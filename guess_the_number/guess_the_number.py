import random
secret_number = random.randint(0,100)

def guess_a_num():
    while True :
        guess = input('Guess a number between 0 and 100: ')
        try:
            return int(guess)
        except:
            try:
                float(guess)
                print('The guess can\'t be decimal')
            except:
                print('You need to guess a number!')
def is_guess_a_pos_whole_num(guess):
    return (guess % 1 == 0) and (guess >= 0) and (guess <= 100)

while True:
    guess = guess_a_num()
    if is_guess_a_pos_whole_num(guess):
        if guess == secret_number:
            print('You win!')
            break
        elif guess > secret_number:
            print('You guessed too high, guess again!')
        else:
            print('You guessed too low, guess again!')
    else:
        print('You need to guess a positive, whole number between 0 and 100!')



