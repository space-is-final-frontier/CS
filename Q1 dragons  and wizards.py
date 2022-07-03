def card_game():
    running = True
    dragon = 0
    wizard = 0

    while running:

        shape = input("What is the shape of the card? ")
        value = input("What is the value of the card? ")

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
            running = False
            
            if dragon > wizard:
                print('Team Dragon won with {} points'.format(dragon))

            else:
                print('Team Wizard won with {} points'.format(wizard))


card_game()