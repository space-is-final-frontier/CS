def has_triple_pair(word):    
    i = 0       #i variable to control the index of letter in word
    count = 0       #count for counting the number of consecutive double letter

    while i < len(word) - 1:
        
        #checking if current and next letter in word are same
        if word[i] == word[i + 1]:

            count = count + 1

            #if count becomes 3, immediatly braking loop by returning True
            if count == 3:
                return True
            
            #increasing the index by 2 if a double pair is found
            i += 2

        #setting count to 0 as consecutive double pairs are to be found
        else:
            count = 0
            i += 1

    return False


word = input("What word do you want to check for 3 consecutive double letters? ")

#confirming double pairs or not by calling function and getting True or False returns
if has_triple_pair(word):
    print('Word has 3 consecutive double letters')

else:
    print('The word does not have 3 consecutive double letters')