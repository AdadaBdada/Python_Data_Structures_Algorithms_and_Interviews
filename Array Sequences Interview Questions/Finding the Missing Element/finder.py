# This approach complexity is O(nlog(n))
def finder(arr1, arr2):
    """
    arr1: integer array
    arr2: integer array
    return: missing integer
    """
    arr1.sort() # nlog(n), pay attention not arr1 = arr1.sort()
    arr2.sort() # nlog(n)

    #  zip function itself runs in O(1) time
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


# This approach complexity is O(n)
import collections

def finder2(arr1,arr2):
    """
    arr1: integer array
    arr2: integer array
    return: missing integer
    """

    d = collections.defaultdict(int)

    # O(n)
    for num in arr2:
        d[num]+=1

    for num in arr1:

        # dictionary contains complexity is O(1)
        # list contains complexity is O(n)
        if d[num] == 0:
            return num
        else:
            d[num]-=1
