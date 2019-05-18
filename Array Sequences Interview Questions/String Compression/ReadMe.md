## Sentence Compression

Time and space complexity of O(n), where n is the number of element in that string

The solution is actually know as **compressing without checking** and it's called **run length compression algorithm**

* We just setting this run equal to an entire string
* l equal to the length of s
* checking two edge cases

```
def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s + "1"

```

* The index is less than the length of the string, if the string **at** that index is equal to the index before it. So that means if the element is equal to the element before it we go ahead and add a count.
* Otherwise we built out this section of the run which is gonna be r. **In this case** if you look at what we are equal to an empty string. So on the first run an empty string plus that very last previous element plus the **string of the count**, so all these counts added together and we reset the count
* Once we did that we went ahead and add 1 one to i and then we're back to the while loop until we're no longer less than the length of the string.
* Then finally we add all the rs together in the same fashion **we did it up here**
* Then we just return that run. That's it for the solution


```
    cnt = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]:
            cnt += 1

        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1

    r = r + s[i-1] + str(cnt)

return r

```
