def LIGHT(colour):

    if colour == 'RED':
        return 0
    
    elif colour == 'YELLOW':
        return 1

    else:
        return 2

def trafficLight():
    colour = input("What is the colour of the light? ")

    if colour not in ('RED', 'YELLOW', 'GREEN'):
        print('Error: Wrong colour input')

    value = LIGHT(colour)

    if not value:
        print('STOP, your life is precious')

    elif value == 1:
        print('Please WAIT, until the light is green')

    elif value == 2:
        print('GO! Thank you for being patient')


trafficLight()
print('SPEED THRILLS BUT KILLS')