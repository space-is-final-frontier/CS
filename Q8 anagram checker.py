def is_anagram(word1, word2):

    sorted1 = sorted(word1)
    sorted2 = sorted(word2)

    if sorted1 == sorted2:
        return True

    else:
        return False


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print('The two words are an anagram')

else:
    print('The two words are not an anagram')