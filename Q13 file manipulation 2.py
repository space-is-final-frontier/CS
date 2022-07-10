def file_copy():
    abcd_file = open('abcd.txt', 'r')       #opening abcd file in read mode
    copy_file = open('Copy.txt', 'w')       #opening Copy file in write mode

    #reading the entire file and writing it to Copy file
    data = abcd_file.read()
    copy_file.write(data)
    print('\n' + 'The file has been copied', end = '\n\n')

    abcd_file.close()       #closing abcd file
    copy_file.flush()       #flushing the internal buffer
    copy_file.close()       #closing Copy file

def find_frequency():
    abcd_file = open('abcd.txt', 'r')       #opening abcd file in read mode
    data = abcd_file.read()       #reading the entire file

    #counting the number of appearances of the word
    word = input("\n" + "Which word's frequency do you want to check? ")
    count = data.count(word)

    #displaying the result
    print('The number of the times the word "{}" appears is {}'.format(word, count), end = '\n\n')

    abcd_file.close()       #closing abcd file

def copy_the_lines():
    abcd_file = open('abcd.txt', 'r')       #opening abcd file in read mode
    copy_file = open('Copy.txt', 'a')       #opening Copy file in append mode
    
    #checking the first four characters of every line if it starts with 'the' and appending it to Copy file
    for line in abcd_file:
        if line[:4].lower() == 'the ':
            copy_file.write(line)

    print('\n' + 'The data of the file has been copied', end = '\n\n')

    abcd_file.close()       #closing abcd file
    copy_file.flush()       #flushing the internal buffer
    copy_file.close()       #closing Copy file

def replace_this():
    abcd_file = open('abcd.txt', 'r')       #opening abcd file in read mode
    data = abcd_file.read()       #reading all the data
    abcd_file.close()       #closing abcd file

    abcd_file = open('abcd.txt', 'w')       #reopening abcd file in write mode
    new_data = data.replace('this', 'that')       #replacing 'this' with 'that'
    new_data = new_data.replace('This', 'That')

    #writing the changed data and overwriting the existing data
    abcd_file.write(new_data + '\n')
    print('\n' + 'The data of the file has been changed', end = '\n\n')

    abcd_file.flush()       #flushing the internal buffer
    abcd_file.close()       #closing abcd file

def display_without_this():
    abcd_file = open('abcd.txt', 'r')       #opening abcd file in read mode
    data = abcd_file.read()
    
    #replacing 'this' with empty space to remove the word entirely from the data
    new_data = data.replace('this', '')
    new_data = new_data.replace('This', '')

    #displaying the changed data
    print('\n' + 'The content of the file without the word "this": ', end = '\n\n')
    print(new_data, end = '\n\n')

    abcd_file.close()       #closing abcd file


proceed = True
while proceed:

    #printing the options menu
    print('1. copy the content to a new file')
    print('2. find the frequency of a word appearing in the file')
    print('3. copy lines starting with the word "the" to a new file')
    print('4. replace the word "This" with "That" in the file')
    print('5. display the content without the word "This"')
    print('0. exit')
    choice = input()

    #checking the choice and calling respective function
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

    #setting the proceed variable to False for ending execution
    elif choice == '0':
        proceed = False

    else:
        print('Invalid input. Please try again')