def has_triple_pair(word):
    
    i = 0
    count = 0

    while i < len(word) - 1:

        if word[i] == word[i + 1]:

            count = count + 1

            if count == 3:

                return True

            i += 2

        else:

            count = 0
            i += 1

    return False


word = input("What word do you want to check for 3 consecutive double letters? ")

if has_triple_pair(word):
    print('Word has 3 consecutive double letters')

else:
    print('The word does not have 3 consecutive double letters')