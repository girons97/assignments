import random
while True:
    number_of_rolls = int(input('How many rolls? '))
    for roll in range(number_of_rolls):
        print('Dice roll: ' + str(roll+1) + ' lands on ' + str(random.randrange(1,7)))
    roll_again = input('Would you like to roll again? (y/n) ')
    if roll_again == 'y':
        continue
    else:
        break
