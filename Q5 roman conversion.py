def roman_conversion(number):
    
    #roman and number list for ease of conversion
    number_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = 12      #length of both lists above is 13, hence max index is 12
    roman_number = ''      #converted roman number

    while number != 0:

        #checking the maximum number in number list not more than the given number
        if number_list[i] <= number:
            
            roman_number += roman_list[i]       #adding the "maximum" roman number
            number = number - number_list[i]    #reducing the given number with the "maximum" number

        #subtracting the index by one when the number at the current index is larger than the number given
        else:
            i -= 1

    #returning the final converted number
    return roman_number


number = int(input("Enter the number to be converted: "))
print(roman_conversion(number))