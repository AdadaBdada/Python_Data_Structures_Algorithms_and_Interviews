## Unique Characters in a string

* First we have our set called **chars**
* And we're going through every element basically every letter in that string
* And saying if letter was in the set then return False else add that letter to that set.
* Now what is this basically doing is essentially the same as chekcing if it already exists in the set

```
def uni_char(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    retrun True
```
