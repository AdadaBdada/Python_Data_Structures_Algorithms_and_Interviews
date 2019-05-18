## Sentence Reversal

* we're setting words as an empty list
* length is just a marker of that length
* spaces is just a list with a whitespace in it

```
def rev_word(s):

    words = []
    length = len(s)
    spaces = [' ']


```

* So we saying while i is less than length. So while we haven't gone through out the entire string
* If s of i (s[i]) is not equal to space then we know the word start, the start of that word is that index.
* So then while i less than length and s[i] not in space,which basically means keep going until we haven't hit another space add 1 to the index.
* Then once the while loop has completed we are going to append. So that word's list from the words start index all the way to the new i, basically once we hit that.
* Then we add i to that index and keep going until i no longer less than length

```
    i = 0

    while i < length:

        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in space:

                i += 1
            word.append(s[word_start:i])
        i+=1
    return ' '.join(reversed(words))

```
