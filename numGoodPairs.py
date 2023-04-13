def numIdenticalPairs(nums):

    obj = {}
    count = 0

    for i in nums:
        if i in obj:
            count += obj[i]
            obj[i] += 1

        else:
            obj[i] = 1

    return count

print(numIdenticalPairs([1,2,3,1,1,3]))
