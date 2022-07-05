def frequency(word_list):
    word_list.sort()
    frequency_dict = {}
    word_index = 0

    while word_index < len(word_list) - 1:

        freq = word_list.count(word_list[word_index])

        if freq not in frequency_dict.keys():
            frequency_dict[freq] = [word_list[word_index]]

        else:
            freq_list = frequency_dict[freq]
            freq_list.append(word_list[word_index])
            frequency_dict[freq] = freq_list

        word_index += freq
    
    return frequency_dict


length = int(input("How long do you want the list? "))
word_list = []

for i in range(length):
    word = input("Input a word: ")
    word_list.append(word)

frequency_dict = frequency(word_list)
print('The frequencies of each word is/are:', frequency_dict)