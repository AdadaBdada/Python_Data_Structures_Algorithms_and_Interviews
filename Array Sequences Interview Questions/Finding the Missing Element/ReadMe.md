## Largest Continuous Sum

* First thing we're doing is edge case check if the array length is equal to zero we just return 0

```
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
```

* For the rest of it  this what we doing. We starting by saying the max_sum and the current_sum is equal to the first element

```
max_sum = current_sum = arr[0]
```

* Then going along for each number in that array not including the first element.
  * We take the current_sum and find out which is larger, the current_sum plus the current number or the current number itself. **Then reset the current_sum equal to whichever one of those is larger.**
  * Then we have the max_sum tracker and we gonna keep track of current_sum and max_sum. **To one of those who is larger gets reset for the max_sum**
  * After we go for each number in the array, we'll have our final max_sum and we will return the max_sum

```
for num in arr[1:]:

    current_sum = max(current_sum+num, num)
    max_sum = max(current_sum, max_sum)

    return max_sum
```


* We sum up the numbers and store in some sort of current_variable. Then add each element we check wheter the current_sum is larger than max_sum encounter so far. **If it is** then we just update the max_sum. As long as the current_sum is positive we can just adding the numbers, when the current_sum become negative we start off a new current_sum because a negative current_sum will only decrease the sum of a future sequence


#### Note

we're not resetting that current_sum to zero because the array could contain all negative integers. Then the result will just **end up being that largest negative number.**
