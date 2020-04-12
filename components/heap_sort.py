#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/3
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------
from components.sort_test import SortTest


class HeapSort(SortTest):
    """ 堆排序， 首先构建一个堆，然后每次取最后一个元素，与第一个元素互换，然后重新构建堆，循环即可得到有序数列 """

    def sort(self, Q: list):
        Q.insert(0, 0)  # 跳过第0个位置
        N = len(Q) - 1

        # 初始构建堆
        for k in range(N // 2, 0, -1):
            self.sink(Q, k, N)

        # 弹出重建
        for k in range(N, 1, -1):
            Q[k], Q[1] = Q[1], Q[k]
            self.sink(Q, 1, k - 1)

        Q.pop(0)

    def sink(self, Q: list, k: int, n: int):
        """ 下沉，将k元素放在正确的位置上，维持堆结构 """
        while 2 * k <= n:  # k还存在下层子节点，必须要等于，不然可能存在未排序节点
            j = 2 * k  # 左子节点
            if j < n and Q[j] < Q[j + 1]:  # 存在右子节点，且大于左子节点
                j += 1
            if Q[j] < Q[k]:  # 如果子节点元素比当前节点小，则说明已经到了正确的位置
                break

            Q[k], Q[j] = Q[j], Q[k]
            k = j


if __name__ == '__main__':
    HeapSort().test()
