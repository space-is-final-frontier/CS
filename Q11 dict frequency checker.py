def dict_value_list(dictionary):      #function to return all the values in a dictionary
    value_list = []

    #iterating over the keys and adding them to a value list
    for key in dictionary:
        value_list.append(dictionary[key])

    return value_list

def frequency(dictionary):
    value_list = dict_value_list(dictionary)      #getting the value list
    value_list.sort()      #sorting list beforehand for easy counting
    frequency_dict = {}      #initialisisng the frequency dictionary and setting index to 0 
    value_index = 0

    while value_index < len(value_list) - 1:

        #counting the frequency and adding it to the dictionary as value
        freq = value_list.count(value_list[value_index])
        frequency_dict[value_list[value_index]] = freq

        #increasing the index variable by frequency number so as not not count the same item again
        value_index += freq

    return frequency_dict


#calling the function to get the frequency dict
dictionary = eval(input("Please enther the dictionary: "))
frequency_dict = frequency(dictionary)
print('The frequencies of each word is/are:', frequency_dict)