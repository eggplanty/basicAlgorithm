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
import heapq


class Solution:
    """
    力扣 215 数组中的第k个最大元素

    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    涉及 快速选择O(N) 堆排序Nlog(K)
    """

    def findKthLargestByHeap(self, nums: List[int], k: int) -> int:
        he = []
        k = len(nums) - k + 1
        for n in nums:
            heapq.heappush(he, -n)  # 默认是小顶堆，输入负
            if len(he) > k:
                heapq.heappop(he)

        return -heapq.heappop(he)  # 输出取负， 将小顶堆当大顶堆用

    def findKthLargestByQuickSelect(self, nums: List[int], k: int) -> int:
        i, j, k = 0, len(nums) - 1, len(nums) - k
        while i <= j:
            n = self.partition(nums, i, j)
            if n == k:
                return nums[k]
            elif n < k:
                i = n + 1
            else:
                j = n - 1
        return 0

    def partition(self, Q: List[int], l: int, r: int) -> int:
        i, j, q = l, r - 1, Q[r]
        while i <= j:
            while i <= j and Q[i] < q:
                i += 1
            while i <= j and Q[j] > q:
                j -= 1
            if i <= j:
                Q[i], Q[j] = Q[j], Q[i]
                i += 1
                j -= 1
        Q[i], Q[r] = Q[r], Q[i]
        return i  # 快速选择，返回分割元素未知


if __name__ == '__main__':
    ret = Solution().findKthLargestByQuickSelect([3, 2, 1, 5, 6, 4], 2)
    print(ret)
