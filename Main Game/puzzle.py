

def get_user_input1():
    return input('Choices: King, Queen, Ace, Joker\n'
                    'What keycard do you want to insert into Slot (1)? ("exit" to leave puzzle:)\n')

def get_user_input2():
    return input('Choices: King, Queen, Ace\n'
                    'What keycard do you want to insert into Slot (2)?\n')

def get_user_input3():
    return input('Choices: King, Ace,\n'
                    'What keycard do you want to insert into Slot (3)?\n')

def get_user_input4():
    return input('What keycard do you want to insert into Slot (4)? (duh!)\n')
                    


def displayPuz1():

    output = "|****** Wall ********|                   |********* Wall **********|\n" + \
             "|--------------------|-------------------|-------------------------|\n" + \
             "| [ unmarked card ]  |                   |         [ X ]   (3)     |\n" + \
             "|--------------------| direction facing  |-------------------------|\n" + \
             "|       [ X ]  (1)   |      <----->      |         [ X ]   (4)     |\n" + \
             "|--------------------|                   |-------------------------|\n" + \
             "|       [ X ]  (2)   |                   |    [ JACK of SPADES ]   |\n" + \
             "|--------------------|-------------------|-------------------------|\n"

    return output

def displayPuz2():
    
    output = "|****** Wall ********|                   |********* Wall **********|\n" + \
             "|--------------------|-------------------|-------------------------|\n" + \
             "| [ unmarked card ]  |                   |         [ X ]   (3)     |\n" + \
             "|--------------------| direction facing  |-------------------------|\n" + \
             "|     [ JOKER ]      |      <----->      |         [ X ]   (4)     |\n" + \
             "|--------------------|                   |-------------------------|\n" + \
             "|       [ X ]  (2)   |                   |    [ JACK of SPADES ]   |\n" + \
             "|--------------------|-------------------|-------------------------|\n"

    return output

def displayPuz3():
    
    output = "|****** Wall ********|                   |********* Wall **********|\n" + \
             "|--------------------|-------------------|-------------------------|\n" + \
             "| [ unmarked card ]  |                   |         [ X ]   (3)     |\n" + \
             "|--------------------| direction facing  |-------------------------|\n" + \
             "|     [ JOKER ]      |      <----->      |         [ X ]   (4)     |\n" + \
             "|--------------------|                   |-------------------------|\n" + \
             "|[ QUEEN of SPADES ] |                   |    [ JACK of SPADES ]   |\n" + \
             "|--------------------|-------------------|-------------------------|\n"

    return output

def displayPuz4():
    
    output = "|****** Wall ********|                   |********* Wall **********|\n" + \
             "|--------------------|-------------------|-------------------------|\n" + \
             "| [ unmarked card ]  |                   |    [ KING of SPADES]    |\n" + \
             "|--------------------| direction facing  |-------------------------|\n" + \
             "|     [ JOKER ]      |      <----->      |         [ X ]   (4)     |\n" + \
             "|--------------------|                   |-------------------------|\n" + \
             "|[ QUEEN of SPADES ] |                   |   [ JACK of SPADES ]    |\n" + \
             "|--------------------|-------------------|-------------------------|\n"

    return output

def main():

    puzzleKeys = ['king', 'queen', 'ace', 'joker']
    count = 0
    while True:

        print(displayPuz1())
        choice1 = get_user_input1()
        guess1 = str(choice1)
        if guess1 == 'exit':
            print("Come back when you're ready.")
            break

        if guess1.strip().lower() == puzzleKeys[3]:
                
            print("The " + str(puzzleKeys[3]) + " keycard is inserted into the slot and a green light illuminates on the panel.")
            print(displayPuz2())
            choice2 = get_user_input2()
            guess2 = str(choice2)

            if guess2.strip().lower() == puzzleKeys[1]:

                print("The " + str(puzzleKeys[1]) + " keycard is inserted into the slot and a green light illuminates on the panel.")
                print(displayPuz3())
                choice3 = get_user_input3()
                guess3 = str(choice3)

                if guess3.strip().lower() == puzzleKeys[0]:
                    print("The " + str(puzzleKeys[0]) + " keycard is inserted into the slot and a green light illuminates on the panel.")
                    print(displayPuz4())
                    choice4 = get_user_input4()
                    guess4 = str(choice4)

                    if guess4.strip().lower() == puzzleKeys[2]:
                        print("The " + str(puzzleKeys[2]) + " keycard slides nicely into slot, and at once all six panels start flashing green in unison.")
                        print("Suddently, you see and hear the six thick steel rods that were previously\n"
                                "blocking the giant door quickly slide and recede from the granite foundation,\n"
                                "disappearing into the solid wall, as the latch unlocks and the door slowly creaks open.\n")
                        print("You quickly book it through the tunnel beyond the door and somehow make it back up to the surface, down the street, unscathed.")
                        print("Yay! You're finally free from this nightmare(and game), you learn your lesson to not take what's not yours(not really), and you win!!")

                        break
                    

                elif guess3.strip().lower() == puzzleKeys[2]:
                    if count >= 3:
                        print("Failing yet again at matching the slot and unlocking the door in front of you, you frantically turn around and freeze in fear upon hearing heavy footsteps hurrying down the basement stairs.")
                        print("To your horror, you are met with the armed psychotic gunrunner that has finally located your whereabouts, and, with maniacal smile, introduces you to his merchandise in the form of molten chunks of lead, effectively shredding you in half.")
                        print("As you scream in utter agony one last time on this earth, your memory finally catches up with you, and you realize how stupid it was to try and steal from this guy.")
                        print("So, you lose, obviously.")
                        break

                    print("The keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right. You'll have to start over.")
                    print("You also suddently feel a dreadful sense of urgency, like you won't have many chances to get this right before whoever is keeping you in this house comes back to collect.")
                    count += 1
                    continue

                
                
            elif guess2.strip().lower() == puzzleKeys[0] or guess2.strip().lower() == puzzleKeys[2]:
                if count >= 3:
                    print("Failing yet again at matching the slot and unlocking the door in front of you, you frantically turn around and freeze in fear upon hearing heavy footsteps hurrying down the basement stairs.")
                    print("To your horror, you are met with the armed psychotic gunrunner that has finally located your whereabouts, and, with maniacal smile, introduces you to his merchandise in the form of molten chunks of lead, effectively shredding you in half.")
                    print("As you scream in utter agony one last time on this earth, your memory finally catches up with you, and you realize how stupid it was to try and steal from this guy.")
                    print("So, you lose, obviously.")
                    break

                print("The keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right. You'll have to start over.")
                print("You also suddently feel a dreadful sense of urgency, like you won't have many chances to get this right before whoever is keeping you in this house comes back to collect.")
                count += 1
                continue

        elif guess1.strip().lower() == puzzleKeys[0] or guess1.strip().lower() == puzzleKeys[1] or guess1.strip().lower() == puzzleKeys[2]:
            if count >= 3:
                print("Failing yet again at matching the slot and unlocking the door in front of you, you frantically turn around and freeze in fear upon hearing heavy footsteps hurrying down the basement stairs.")
                print("To your horror, you are met with the armed psychotic gunrunner that has finally located your whereabouts, and, with maniacal smile, introduces you to his merchandise in the form of molten chunks of lead, effectively shredding you in half.")
                print("As you scream in utter agony one last time on this earth, your memory finally catches up with you, and you realize how stupid it was to try and steal from this guy.")
                print("So, you lose, obviously.")
                break

            print("The keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right.  You'll have to start over.")
            print("You also suddently feel a dreadful sense of urgency, like you won't have many chances to get this right before whoever is keeping you in this house comes back to collect.")
            count += 1
            continue

        else:
            print('You didnt enter a valid number. Try again!')

main()