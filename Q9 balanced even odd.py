def balanced(a):
    if len(a) == 0:
        return True

    else:
        even_count = 0
        odd_count = 0

        for number in a:

            if number % 2 == 0:
                even_count += 1

            else:
                odd_count += 1

        if even_count == odd_count:
            return True
        
        else:
            return False


length = int(input("How long do you want the list? "))
int_list = []

for i in range(length):
    integer = int(input("Input a number: "))
    int_list.append(integer)


if balanced(int_list):
    print('The list is balanced between even and odd numbers')

else:
    print('The list is unbalanced between even and odd numbers')