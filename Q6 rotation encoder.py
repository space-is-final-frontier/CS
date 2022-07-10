def rotate_word(word, shift):
    rotated_word = ''      #rotated number

    #iterating over every word in given word
    for letter in word:

        #checking if the letter is upercase or lowercase and assigning appropriate ascii shift
        if letter.isupper():
            ascii_shift = 65

        else:
            ascii_shift = 97

        ascii_number = ord(letter)          #converting the letter to ascii number
        ascii_number -= ascii_shift         #shifting the ascii number to range of 0 to 25
        ascii_number += shift               #adding amount to be shifted
        ascii_number %= 26                  #converting the ascii number back to range of 0 to 25
        ascii_number += ascii_shift         #reshfiting the ascii number back to original range
        rotated_word += chr(ascii_number)   #converting the new ascii number back to alphabet
    
    #returning the final converted number
    return rotated_word


word = input("What is the original message word? ")
shift = int(input("By how much do you want to shift? "))
print(rotate_word(word, shift))