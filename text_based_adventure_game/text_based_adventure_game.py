import random

def setup_game(): # This function asks user for their name and number of dungeon levels. It also creates a 'correct pathway' dictionary {level: correct_decision}
    print('Welcome to the Adventure Game!\n In this game you will choose your own path, if luck permits you will find the treasure and escape the dungeon with your life intact...')
    player_name = input('\"Hello traveller, what name do you go by?\"\nInput name:\n')
    while True:
        num_levels_string = input('\"How many levels in the dungeon are you willing to go {}?\"\nInput number of levels:\n'.format(player_name))
        try:
            num_levels = int(num_levels_string)
            correct_path = {(level+1) : random.randint(1,3) for level in range(num_levels)}
            return player_name, correct_path, num_levels
        except:
            print('You need to input an integer for the number of levels...')



def choose_door(): #This function asks user which direction they want to proceed in (left, straight or right) if 1, 2 or 3 entered direction_choice is returned
    while True:
        direction_choice_string = input('Which way will you go?\nInput 1 for Left\nInput 2 for Straight\nInput 3 for Right\n')
        try:
            direction_choice = int(direction_choice_string)
            if direction_choice == 1 or direction_choice == 2 or direction_choice == 3:
                return direction_choice
            else:
                print('You must input 1, 2 or 3 (Left: 1, Straight: 2, Right: 3')
        except:
            print('You need to input an integer (Left: 1, Straight: 2, Right: 3')
    
def dead_end_room(current_level): #If an incorrect decision was made the user enters a dead_end_room, their level remains the same
    dead_end_room_dict = {
    1: 'has writing on the wall in chalk. It is smeared as though someone has tried to rub it out. The words are in Common, and say \“Safety is a lie\”.',
    2: 'has a deep gouge down the centre of the paved floor. It looks like something heavy was dragged across the room, though there is no evidence of it here now.',
    3: 'holds a wide well in the southeast corner. There is no water in the well, but a crude rope ladder descends into the darkness. From far below you can hear the thud and scrape of a pick against rock.',
    4: 'is coated in sheets of thick black slime that seem to ooze out of the surface of the rock itself. The air smells of fungus and mould, and the temperature is a few degrees warmer than the corridor outside.',
    5: 'has a huge iron cage against the western wall. The door of the cage is held shut with several lengths of thick chain that has rusted tight over several years. The skeletal remains of a gnoll lie in the corner of the cage, along with a dusty glass bottle that still holds a few drops of viscous red liquid.',
    6: 'holds a vicious spike trap that descends from the ceiling, but it has already triggered. The mechanism hangs in the centre of the room, the tips of the spikes just scraping the floor. The edges are jagged and rusty, and something humanoid and very, very dead appears trapped beneath the trap.'
    }
    print('You enter a room on level ' + str(current_level) + ' which ' + dead_end_room_dict[random.randint(1,6)] + '\n*sigh*\n\"This can\'t be right\", you think to yourself.\n(You decide to exit the way you came)')
    return current_level

def progression_room(current_level): #If an correct decision was made the user enters a progression_room, their level increases by 1
    progression_room_dict = {
    1: 'is a corridor so long that you can’t make out the far end. It is lined with cracked obsidian pillars, each carved with a figure that appears to be running towards the end of the hall.',
    2: 'is completely covered in mirrors set at odd angles, so that you can never see your own reflection but see multiple versions of anybody else in the room with you. Once the door closes it is incredibly difficult to find again. If there is another exit, you will need to hunt for it.',
    3: 'is a wide, deep basin that was once an arena of some kind. Three incredibly lifelike statues stand in the centre of the battle ground, frozen in place as though caught in the midst of a fight against some massive enemy that is no longer present.',
    4: 'small chamber is barely more than a walk-in cupboard. The walls are painted with vibrant colours depicting disembodied eyes and mouths. A strange silver helmet is suspended from the ceiling by chains. It hums softly to itself, and vibrates gently when the door is closed.',
    5: 'is choked with corpses that appear far too fresh for comfort. The air is thick with the smell of death and the tang of blood, and an unsettling squelching noise accompanies each of your steps. All of the corpses are naked, and there is no sign of whatever weapon caused the deep gashes across their bodies.',
    6: 'appears to have no second half. About twenty feet into the room everything just ceases to exist. The floor, walls, and ceiling are replaced with an inky void, but you can’t tell if the blackness is the absence or the presence of… something.'
    }
    print('You enter a room on level ' + str(current_level) + ' which ' + progression_room_dict[random.randint(1,6)] + '\n*sigh of relief*\n\"This looks like the right way\", you think to yourself, as you notice a door at the end of the room.\n(You decide to venture through the door at the opposing end of the room)')
    current_level += 1
    return current_level

def end_game(current_level): #If a correct decision was made on the final level the user enters the end_game, their level increases by 1 (exited dungeon)
    print('You enter a room which is shrouded in darkness except for a slight glow at the end.\nYou walk towards the glowing object and upon further inspection, you notice it is a chest brimming with shimmering gold.\nYou fill your inventory with the loot and ascend the rope ladder behind the chest.\nAfter what seems like an eternity, you finally reach the surface, dawn is just breaking. You won!')
    current_level += 1
    return current_level

def correct_choice(current_level, direction_choice, correct_path, num_levels): #Compares direction choice to 'correct pathway' dictionary, depending on the direction_choice the function returns the function of which room to proceed to.
    if correct_path[current_level] == direction_choice:
        if (current_level == num_levels) and (correct_path[current_level] == direction_choice):
            return end_game(current_level)
        else:
            return progression_room(current_level)
    else:
        return dead_end_room(current_level)


player_name, correct_path, num_levels = setup_game() #Sets up the game
print('Your player name is {}, the correct path (level: choice) is {}, the number of levels is {}'.format(player_name, correct_path, num_levels)) #Cheat statement, this line can be commented out to keep 'correct pathway' hidden
current_level = 1 #Always start on level 1
while True:
    print('You have entered level {}'.format(current_level)) #Prints current level
    direction_choice = choose_door() #User chooses direction 
    current_level = correct_choice(current_level, direction_choice, correct_path, num_levels) #If user went to progression room or end game room the current level increases by 1, if went to dead end room level remains same
    if current_level == num_levels + 1:
        break

