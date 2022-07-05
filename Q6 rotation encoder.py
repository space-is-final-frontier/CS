def rotate_word(word, shift):
    rotated_word = ''

    for letter in word:

        if letter.isupper():

            ascii_number = ord(letter)
            ascii_number -= 65
            ascii_number += shift
            ascii_number %= 26
            ascii_number += 65
            rotated_word += chr(ascii_number)

        if letter.islower():
            
            ascii_number = ord(letter)
            ascii_number -= 97
            ascii_number += shift
            ascii_number %= 26
            ascii_number += 97
            rotated_word += chr(ascii_number)
    
    return rotated_word


word = input("What is the original message word? ")
shift = int(input("By how much do you want to shift? "))
print(rotate_word(word, shift))