def sorting(int_list):      #sorting function uses insertion sort

    #since the first element is considered sorted already, we count index from 1 not 0
    for index in range(1, len(int_list)):

        #checking if the element before the given index is greater
        while int_list[index - 1] > int_list[index] and index > 0:

            #swapping the values
            int_list[index - 1], int_list[index] = int_list[index], int_list[index - 1]
            
            #decreasing the index by one to continue sorting the element and now the one before it
            index -= 1


int_1 = int(input("Please enter the first integer: "))
int_2 = int(input("Please enter the second integer: "))
int_3 = int(input("Please enter the third integer: "))
int_4 = int(input("Please enter the fourth integer: "))
int_5 = int(input("Please enter the fifth integer: "))

integers = [int_1, int_2, int_3, int_4, int_5]      #placing the 5 integers in a list to sort easily
sorting(integers)       #calling sorting function

print('Minimum integer is {}'.format(integers[0]))      #displaying the max and min integers
print('Maximum integer is {}'.format(integers[-1]))