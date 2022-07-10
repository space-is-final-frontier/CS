def is_anagram(word1, word2):
    sorted1 = sorted(word1)     #sorting the words so that if they are anagrams, sorted1 and 2 will be same
    sorted2 = sorted(word2)

    #returning True or False based on sorted 1 and 2 are same or not
    if sorted1 == sorted2:
        return True

    else:
        return False


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

#confirming anagrams or not by calling function and getting True or False returns
if is_anagram(word1, word2):
    print('The two words are an anagram')

else:
    print('The two words are not an anagram')