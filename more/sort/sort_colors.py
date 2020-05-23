#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/15
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------
from typing import List


class Solution:
    """
    75 颜色分类

    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

    荷兰国旗问题
    荷兰国旗包含三种颜色：红、白、蓝。
    有三种颜色的球，算法的目标是将这三种球按颜色顺序正确地排列。它其实是三向切分快速排序的一种变种，在三向切分快速排序中，每次切分都将
    数组分成三个区间：小于切分元素、等于切分元素、大于切分元素，而该算法是将数组分成三个区间：等于红色、等于白色、等于蓝色。

    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, len(nums) - 1, 0
        while k <= j:
            if nums[k] == 0:  # 与左边交换
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                i += 1  # 左边交换过来的是已经扫描过的，所以可以直接下一个
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1  # 右边交换过来的是未扫描过的，所以需要再判断一次
            else:
                k += 1


if __name__ == '__main__':
    nums = [1, 2, 0]
    ret = Solution().sortColors(nums)
    print(nums)
