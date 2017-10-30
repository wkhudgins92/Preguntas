# Determines if two words are an anagram

import sys

def are_anagrams(word1, word2):
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

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python anagrams.py word1 word2" 
        sys.exit(1)
    areAnagrams = are_anagrams(sys.argv[1], sys.argv[2])
    if areAnagrams:
        print "%s and %s are anagrams" % (sys.argv[1], sys.argv[2])
    else:
        print "%s and %s are not anagrams" % (sys.argv[1], sys.argv[2])
