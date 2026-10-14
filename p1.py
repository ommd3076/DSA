def countno():
    counts = {}
    nums = [4, 2, 4, 3, 2, 4]
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
            
        else:
            counts[num] = 1
    return counts