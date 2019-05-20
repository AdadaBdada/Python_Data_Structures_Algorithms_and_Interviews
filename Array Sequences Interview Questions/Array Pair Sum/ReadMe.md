## Array Pair Sum

* First we have a edge case check in case there is less than two element
* And then we have our sets for tracking the number we've seen in our output
* we're going along the array and we're saying for that number in the array the target number we are looking for will be k minus num
* So then we say if target is not seen we haven't seen that number yet we go ahead and add it to that set
* And then else, what we do is we add it to the output. So we say the output dot add and we take the minimum between the current number and the target as one of the pairs. And we take the maximum between the number and the target. So we want to find out which was the minimum


```
def pair_sum(arr, k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))

    return len(output)

```
