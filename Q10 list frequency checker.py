def frequency(word_list):
    word_list.sort()       #sorting list beforehand for easy counting
    frequency_dict = {}       #initialisisng the frequency dictionary and setting index to 0 
    word_index = 0

    while word_index < len(word_list) - 1:

        #counting the frequency of the words
        freq = word_list.count(word_list[word_index])

        #if the frequency number is not already present then making a new key
        if freq not in frequency_dict.keys():
            frequency_dict[freq] = [word_list[word_index]]

        #if frequency number exists then adding the word to the value list
        else:
            freq_list = frequency_dict[freq]
            freq_list.append(word_list[word_index])
            frequency_dict[freq] = freq_list

        #increasing the index variable by frequency number so as not not count the same word again
        word_index += freq
    
    return frequency_dict


length = int(input("How long do you want the list? "))
word_list = []

for i in range(length):
    word = input("Input a word: ")
    word_list.append(word)

#calling the function to get the frequency dict
frequency_dict = frequency(word_list)
print('The frequencies of each word is/are:', frequency_dict)