def card_game():
    running = True      #running variable to control how long the function is to be executed
    dragon = 0      #scores of teams dragon and wizard
    wizard = 0

    while running:

        shape = input("What is the shape of the card? ")
        value = input("What is the value of the card? ")

        #adding points to respective team based on given rules
        if shape in ('diamond', 'club'):
            dragon += 1

        elif shape == 'heart':

            if value not in ('A', 'Jack', 'Queen', 'King'):
                wizard += 1

            else:
                dragon += 1

        else:
            wizard += 1

        proceed = input("Continue? (y/n) ")

        if proceed == 'n':

            #setting running variable to False to end execution
            running = False 
            
            #displaying the winning team and it's points
            if dragon > wizard:
                print('Team Dragon won with {} points'.format(dragon))

            else:
                print('Team Wizard won with {} points'.format(wizard))


card_game()     #calling function to start the program