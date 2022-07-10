def LIGHT(colour):
    
    #returning values 0, 1 and 2 based on what colour is given
    if colour == 'RED':
        return 0
    
    elif colour == 'YELLOW':
        return 1

    else:
        return 2

def trafficLight():
    colour = input("What is the colour of the light? ")

    #checking if colour is other than red, yellow or green
    if colour not in ('RED', 'YELLOW', 'GREEN'):
        print('Error: Wrong colour input')

    value = LIGHT(colour)

    #printing respective messages according to the value returned by LIGHT function
    if value == 0:
        print('STOP, your life is precious')

    elif value == 1:
        print('Please WAIT, until the light is green')

    elif value == 2:
        print('GO! Thank you for being patient')


trafficLight()      #calling function to start the program
print('SPEED THRILLS BUT KILLS')    #printing the warning message after execution is over