def last_three_chars():
    print('\n' + 'The last 3 characters of each line is:', end = '\n\n')
    abcd_file = open('abcd.txt', 'r')

    for line in abcd_file:
        print(line[-4:], end = '')

    print('\n')
    abcd_file.close()

def all_uppercase():
    abcd_file = open('abcd.txt', 'r')

    print('\n' + 'The content of the file in uppercase: ', end = '\n\n')
    print(abcd_file.read().upper(), end = '\n\n')
    
    abcd_file.close()

def count_uppercase():
    abcd_file = open('abcd.txt', 'r')
    counter = 0

    for line in abcd_file:
        for ch in line:
            if ch.isupper():
                counter += 1

    print('\n' + 'The number of uppercase characters are:', counter, end = '\n\n')
    abcd_file.close()

def count_vowels():
    abcd_file = open('abcd.txt', 'r')
    counter = 0

    for line in abcd_file:
        for ch in line:            
            if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
                counter += 1

    print('\n' + 'The number of vowels are:', counter, end = '\n\n')
    abcd_file.close()


proceed = True
while proceed:
    print('1. display last three characters of all the lines')
    print('2. display the content of the text file in upercase')
    print('3. display the count of all the uppercase characters')
    print('4. display the count of all the vowels')
    print('0. exit')
    choice = input()

    if choice == '1':
        last_three_chars()

    elif choice == '2':
        all_uppercase()

    elif choice == '3':
        count_uppercase()

    elif choice == '4':
        count_vowels()

    elif choice == '0':
        proceed = False

    else:
        print('Invalid input. Please try again')