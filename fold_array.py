def fold_array(array, runs):
    run = 1
    new_list = list(array)
    while run <= runs:
        x = [new_list.pop(len(new_list)-1) for i in range(int(len(new_list)/2))]
        if len(x) != len(new_list): x.append(0)
        new_list = [sum(item) for item in zip(x, new_list)]
        run += 1

    return new_list


"""
ohter code
"""

def fold_array(array, runs):
    nums = list(array)
    for _ in xrange(runs):
        for a in xrange(len(nums) // 2):
            nums[a] += nums.pop()
    return nums
