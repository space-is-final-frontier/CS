int_1 = int(input("Please enter the first integer: "))
int_2 = int(input("Please enter the second integer: "))
int_3 = int(input("Please enter the third integer: "))
int_4 = int(input("Please enter the fourth integer: "))
int_5 = int(input("Please enter the fifth integer: "))

integers = [int_1, int_2, int_3, int_4, int_5]
integers.sort()

print('Minimum integer is {}'.format(integers[1]))
print('Maximum integer is {}'.format(integers[-1]))