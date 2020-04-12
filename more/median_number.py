#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/6
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------
import heapq


class MedianNumber:
    """
    获取中位数
    通过heapq构建一个大顶堆, 一个小顶堆, 保证大顶堆中所有元素都小于小顶堆
    中位数即为小顶堆最小值, 或者两个堆顶元素的均值
    """

    def __init__(self):
        self.small_heap = []
        self.big_heap = []
        self.N = 0

    def Insert(self, num):
        # write code here
        if self.N % 2 == 0:
            heapq.heappush(self.big_heap, -num)  # 大顶堆的构建，通过插入值取负，返回值取负，来将小顶堆构建成大顶堆
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))  # 返回值取负
        else:
            heapq.heappush(self.small_heap, num)
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        self.N += 1

    def GetMedian(self):
        # write code here
        if self.N % 2 == 1:
            return heapq.heappop(self.small_heap)
        else:
            return 0.5 * (heapq.heappop(self.small_heap) + (-heapq.heappop(self.big_heap)))


if __name__ == '__main__':
    so = MedianNumber()
    [so.Insert(k) for k in [4, 5, 1, 6, 2, 7, 3, 8]]
    print(so.GetMedian())
