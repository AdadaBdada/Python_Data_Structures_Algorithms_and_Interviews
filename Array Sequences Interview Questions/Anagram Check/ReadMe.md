## 242. Valid Anagram

#### Time complexity O(n)

* First of all, we clean up the strings. Lowercase all the letters remove any whitespace
* We do an edge case check, so this would quickly tell us if it's anagrams or not.
* Otherwise we have a possibility of an anagrams, so moving along we create a dictionary called **count**. Then for every letter in that first string, if the letter already in our counting dictionary. we're jest gonna say count that letter so that key add 1 to that count. **Otherwise** set it equal to 1.
* For letter in t, which is that second string do the same thing. But now we're going to be subtracting. So if letter in counts then we're going to subtract 1 from it. Else that count of that letter is euqal to 1. And this is the setting right here. That's basically going to trip up this third for loop in case it's not an anagram. That's why this is again a positive equal to 1. So this is what's going to be going off if this is not an anagram along with this(first for loop equal to 1) as well.
* So then it says for k in counts, if count of k is not equal to zero, return false
