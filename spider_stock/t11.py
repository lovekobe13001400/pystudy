def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    arr = []
    flag = 0
    num = len(nums)
    for i in range(num):
        if flag == 1:
            break
        for j in range(i + 1, num):
            if nums[i] + nums[j] == target:
                arr.append(i)
                arr.append(j)
                return arr

mynum = [1,2,3,4]
print(twoSum(mynum,3))