# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 数组中重复的数字-2
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 方法2：一轮扫描，之后交换对应位置上的元素 时间复杂度ON，空间复杂度O1

def find_duplicate(nums, length):
    if not nums or length <= 0:
        return False
    for i in range(length):
        if nums[i] < 0 or nums[i] > length - 1:
            return False
    for i in range(length):
        while nums[i] != i:
            tmp = nums[i]
            if nums[i] == nums[tmp]:
                return nums[i]
            nums[i], nums[tmp] = nums[tmp], nums[i]


if __name__ == "__main__":
    nums = [2, 3, 5, 4, 2, 6, 7, 1]
    ans = find_duplicate(nums, 8)
    print(ans)
