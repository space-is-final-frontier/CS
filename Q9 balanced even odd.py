def balanced(a):

    #checking if the list is empty so as to not waste resources later in execution
    if len(a) == 0:
        return True

    else:
        even_count = 0      #number of even and odd integers in list
        odd_count = 0

        for number in a:
            
            #if number is even, increasing even_count by 1, else odd_count by 1
            if number % 2 == 0:
                even_count += 1

            else:
                odd_count += 1

        #if even and odd count are same then retruning True else False
        if even_count == odd_count:
            return True
        
        else:
            return False


length = int(input("How long do you want the list? "))
int_list = []

for i in range(length):
    integer = int(input("Input a number: "))
    int_list.append(integer)

#confirming equal even and odd integers or not by calling function and getting True or False returns
if balanced(int_list):
    print('The list is balanced between even and odd numbers')

else:
    print('The list is unbalanced between even and odd numbers')