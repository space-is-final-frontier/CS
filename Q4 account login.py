def login(userid, passwd):
    success = False
    tries = 0

    while not success:

        if userid == 'ADMIN':

            if passwd == 'St0rE@1':

                success = True

                print('Login Successful')

                break
            
            else:
                tries += 1

        else:
            tries += 1

        
        if tries == 3:
            print('account blocked')


userid = input("Please enter your userid: ")
password = input("Please enter your password: ")
login(userid, password)