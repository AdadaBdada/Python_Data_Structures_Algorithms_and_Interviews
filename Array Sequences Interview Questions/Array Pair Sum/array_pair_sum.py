def pair_sum(arr, k):
    """
    arr: integer array
    k: specific value k
    return: unique pairs
    """

    # Edge case check
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add(min(target, num), max(target, num))

    return len(output)
    #return '/n'.join(map(str,list(output)))
