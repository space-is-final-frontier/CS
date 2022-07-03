def dict_value_list(dictionary):
    value_list = []

    for key in dictionary:
        value_list.append(dictionary[key])

    return value_list

def frequency(dictionary):

    value_list = dict_value_list(dictionary)
    value_list.sort()
    frequency_dict = {}
    value_index = 0

    while value_index < len(value_list) - 1:

        freq = value_list.count(value_list[value_index])
        frequency_dict[value_list[value_index]] = freq

        value_index += freq

    return frequency_dict


dictionary = eval(input("Please enther the dictionary: "))
frequency_dict = frequency(dictionary)
print('The frequencies of each word is/are:', frequency_dict)