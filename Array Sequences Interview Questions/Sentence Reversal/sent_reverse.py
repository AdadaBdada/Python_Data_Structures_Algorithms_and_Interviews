# Python trick

def rev_word1(s):
    return " ".join(reversed(s.split())) # string.split() s='    space before' s.split() =['space','before']

def rev_word2(s):
    return " ".join(s.split()[::-1])

def rev_words(s):

    word = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

         # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            word.append(s[word_start:i])
         # Add to index
        i += 1

    return " ".join(word[::-1])
