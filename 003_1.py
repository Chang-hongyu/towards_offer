# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 数组中重复的数字-1
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 法1 利用哈希表来存储，时间复杂度为N，空间复杂度也为N

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def find_duplicate(self):
        # 构造一个辅助字典
        dic = {}
        for i, num in enumerate(self.nums):
            if num in dic:
                return num
            else:
                dic[num] = i
        # 表示没有找到
        return -1


if __name__ == "__main__":
    tmp = Solution([2, 3, 1, 0, 2, 5, 4, 3, 6])
    ans = tmp.find_duplicate()
    print(ans)
