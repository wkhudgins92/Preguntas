# Determines if two words are an anagram

import sys

def are_anagrams_basic(word1, word2):
    # First remove all whitespace
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    
    # Ensure both words are of the same length, if they are not, they aren't anagrams
    if len(word1) != len(word2):
        return False

    # Sort the letters in both words, if the words are anagrams they should 
    # be identical post-sorting
    word1 = list(word1).sort()
    word2 = list(word2).sort()

    if word1 == word2:
        return True
    else:
        return False

def are_anagrams_linear(word1, word2):
    # Ensure both words are of the same length, if they are not, they aren't anagrams
    if len(word1) != len(word2):                                                
        return False                                                            

    # Loop through word1, keeping a count of the frequency of each letter in
    # word1, then do the same for word2. The resultant dictionaries should be
    # identical. This could be done using the built in collections.Counter
    # class but for demonstration and learning purposes, it is not used here
    dict1 = {}
    dict2 = {}
    for letter in word1:
        if not letter in dict1:
            dict1[letter] = 1
        else:
            dict1[letter] += 1

    for letter in word2:
        if not letter in dict2:
            dict2[letter] = 1
        else:
            dict2[letter] += 1

    return dict1 == dict2

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python anagrams.py word1 word2" 
        sys.exit(1)
    areAnagrams = are_anagrams_linear(sys.argv[1], sys.argv[2])
    if areAnagrams:
        print "%s and %s are anagrams" % (sys.argv[1], sys.argv[2])
    else:
        print "%s and %s are not anagrams" % (sys.argv[1], sys.argv[2])
