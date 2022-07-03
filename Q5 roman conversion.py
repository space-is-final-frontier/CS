def roman_conversion(number):
      
    number_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = 12
    roman_number = ''

    while number != 0:

        if number_list[i] <= number:

            roman_number += roman_list[i]
            number = number - number_list[i]

        else:
            i -= 1

    return roman_number


number = int(input("Enter the number to be converted: "))
print(roman_conversion(number))