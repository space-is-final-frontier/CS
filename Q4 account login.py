tries = 0       #global tries variable to count how many tries the user has taken

def login(userid, passwd):
    global tries

    #checking if the userid and password given are correct
    if userid == 'ADMIN':

        if passwd == 'St0rE@1':

            #returning the function to stop execution
            print('Login Successful')
            return
    
        #adding 1 to tries variable if userid or passwd are incorrect
        else:
            tries += 1

    else:
        tries += 1
    
    #blocking the account if tries is 3
    if tries == 3:
        print('account blocked')

    #recalling the function login_input to continue trying to login (recursion)
    else:
        login_input()

def login_input():
    global tries
    print('Attempt number:', tries + 1)
    userid = input("Please enter your userid: ")
    password = input("Please enter your password: ")
    login(userid, password)     #calling the login function for next try at login


login_input()      #calling function to start the program