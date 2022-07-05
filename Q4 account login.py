tries = 0

def login(userid, passwd):
    global tries

    if userid == 'ADMIN':

        if passwd == 'St0rE@1':
            print('Login Successful')
            return
        
        else:
            tries += 1

    else:
        tries += 1
        
    if tries == 3:
        print('account blocked')

    else:
        login_input()

def login_input():
    global tries
    print('Attempt number:', tries + 1)
    userid = input("Please enter your userid: ")
    password = input("Please enter your password: ")
    login(userid, password)

login_input()