

def get_user_input1():
    return input('Choices: King, Queen, Ace, Joker\n'
                    'What keycard do you want to insert into Slot (1)? ("exit" to leave puzzle:)\n')

def get_user_input2():
    return input('Choices: King, Queen, Ace\n'
                    'What keycard do you want to insert into Slot (2)? ("exit" to leave puzzle:)\n')

def get_user_input3():
    return input('Choices: King, Ace,\n'
                    'What keycard do you want to insert into Slot (3)? ("exit" to leave puzzle:)\n')

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

            if guess2 == 'exit':
                print("Come back when you're ready.")
                break

            if guess2.strip().lower() == puzzleKeys[1]:

                print("The " + str(puzzleKeys[1]) + " keycard is inserted into the slot and a green light illuminates on the panel.")
                print(displayPuz3())
                choice3 = get_user_input3()
                guess3 = str(choice3)

                if guess3 == 'exit':
                    print("You almost have it.. come on, you got this!")
                    break

                if guess3.strip().lower() == puzzleKeys[0]:
                    print("The " + str(puzzleKeys[0]) + " keycard is inserted into the slot and a green light illuminates on the panel.")
                    print(displayPuz4())
                    choice4 = get_user_input4()
                    guess4 = str(choice4)

                    if guess4.strip().lower() == puzzleKeys[2]:
                        print("The " + str(puzzleKeys[2]) + " fuse snaps perfectly into the slot.")
                        print("Suddently, you see and hear the six thick steel rods that were previously\n"
                                "blocking the giant door quickly slide and recede from the granite foundation,\n"
                                "disappearing into the solid wall, as the latch unlocks and the door slowly creaks open")
                        print("You're finally free from this nightmare!")

                        break
                    

                elif guess3.strip().lower() == puzzleKeys[2]:
                    print("The keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right. You'll have to start over.")
                    continue

                
                
            elif guess2.strip().lower() == puzzleKeys[0] or guess2.strip().lower() == puzzleKeys[2]:
                print("TThe keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right. You'll have to start over.")
                continue

        elif guess1.strip().lower() == puzzleKeys[0] or guess1.strip().lower() == puzzleKeys[1] or guess1.strip().lower() == puzzleKeys[2]:
            print("The keycard is inserted, followed by a bright red light flashing on the panel.  There's no point in trying the other panels if you can't get this one right.  You'll have to start over.")
            continue

        else:
            print('You didnt enter a valid number. Try again!')

main()