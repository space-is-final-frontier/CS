def file_copy():
    abcd_file = open('abcd.txt', 'r')
    copy_file = open('Copy.txt', 'w')

    data = abcd_file.read()
    copy_file.write(data)
    print('\n' + 'The file has been copied', end = '\n\n')

    abcd_file.close()
    copy_file.flush()
    copy_file.close()

def find_frequency():
    abcd_file = open('abcd.txt', 'r')
    data = abcd_file.read()

    word = input("\n" + "Which word's frequency do you want to check? ")
    count = data.count(word)

    print('The number of the times the word "{}" appears is {}'.format(word, count), end = '\n\n')

    abcd_file.close()    

def copy_the_lines():
    abcd_file = open('abcd.txt', 'r')
    copy_file = open('Copy.txt', 'a')
    
    for line in abcd_file:
        if line[:4].lower() == 'the ':
            copy_file.write(line)

    print('\n' + 'The data of the file has been copied', end = '\n\n')

    abcd_file.close()
    copy_file.flush()
    copy_file.close()

def replace_this():
    abcd_file = open('abcd.txt', 'r')
    data = abcd_file.read()
    abcd_file.close()

    abcd_file = open('abcd.txt', 'w')
    new_data = data.replace('this', 'that')
    new_data = new_data.replace('This', 'That')

    abcd_file.write(new_data + '\n')
    print('\n' + 'The data of the file has been changed', end = '\n\n')

    abcd_file.flush()
    abcd_file.close()

def display_without_this():
    abcd_file = open('abcd.txt', 'r')
    data = abcd_file.read()
    
    new_data = data.replace('this', '')
    new_data = new_data.replace('This', '')

    print('\n' + 'The content of the file without the word "this": ', end = '\n\n')
    print(new_data, end = '\n\n')

    abcd_file.close()


proceed = True
while proceed:
    print('1. copy the content to a new file')
    print('2. find the frequency of a word appearing in the file')
    print('3. copy lines starting with the word "the" to a new file')
    print('4. replace the word "This" with "That" in the file')
    print('5. display the content without the word "This"')
    print('0. exit')
    choice = input()

    if choice == '1':
        file_copy()

    elif choice == '2':
        find_frequency()

    elif choice == '3':
        copy_the_lines()

    elif choice == '4':
        replace_this()

    elif choice == '5':
        display_without_this()

    elif choice == '0':
        proceed = False

    else:
        print('Invalid input. Please try again')