#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/3/23
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------


class BinarySearch:
    """
    二分查找,时间复杂度O(logn)
    """

    def recur_binary_search(self, data: list, target: int, low: int, high: int) -> bool:
        """ 用递归实现二分查找 """

        if low > high:
            return False

        mid = (low + high) // 2
        if data[mid] == target:
            return True

        if target < data[mid]:
            return self.recur_binary_search(data, target, low, mid - 1)
        else:
            return self.recur_binary_search(data, target, mid + 1, high)

    def loop_binary_search(self, data: list, target: int, low: int, high: int) -> bool:
        """ 通过循环实现二分查找 """

        while low <= high:

            mid = (low + high) // 2
            if target == data[mid]:
                return True

            if target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def binary_search_first_no_small(self, nums: list, k: int):
        """ 二分查找第一个不小于k的值的索引, 如果k大于nums[-1] 则返回len(nums) """

        l, r = 0, len(nums)  # len(nums)会使得最终l超出边界, 而len(nums)-1会使得其无论如何都停留在边界
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= k:
                r = m
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    bs = BinarySearch()
    example = [1, 3, 5, 6, 6, 7, 8, 9, 23, 55, 98, 132]
    print(bs.loop_binary_search(example, 1, 0, len(example) - 1))

    ret = bs.binary_search_first_no_small(example, 12)
    print(example[ret])
