def twoSum(nums, target):
    nums_list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                if i not in nums_list:
                    nums_list.append(i)
                if j not in nums_list:
                    nums_list.append(j)
    return nums_list


print(twoSum([-1, -2, -3, -4, -5], -8))
