# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 不修改数组，找出重复的数字
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 法3 不修改数组，找出重复元素，利用二分查找思想，时间复杂度O(NlogN)，空间复杂度为O1

def get_duplicate(nums):
    # 判断边界条件
    if not nums:
        print("数组为空")
        return False

    n = len(nums)
    for i in nums:
        if i < 1 or i > n - 1:
            print("输入值有错误")
            return False

    start = 1
    end = n - 1
    while end >= start:
        mid = (start + end) // 2
        count = countRange(nums, start, mid)
        # 如果只有一个数字时，统计出来的次数大于1，则说明这个数字是重复的
        if end == start:
            if count > 1:
                return start
            else:
                print("无重复数字")
                break
        # 若count值大于start到mid的数量，则说明重复值在start-mid之间(包括mid)
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1
    # 表示没有重复
    return False


def countRange(nums, start, end):
    count = 0
    for i in nums:
        if i >= start and i <= end:
            count += 1
    return count


if __name__ == "__main__":
    nums = [2, 3, 5, 4, 1, 2, 6, 7, 8]
    ans = get_duplicate(nums)
    print(ans)
