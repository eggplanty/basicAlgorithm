#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/2
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------

from components.sort_test import SortTest


class InsertionSort(SortTest):
    """
    插入排序, 平均复杂度O(N^2 / 4), 最坏O(N^2 / 2)， 最好O(N)
    """

    def sort(self, Q: list):

        for i in range(1, len(Q)):  # [1, ..., n-1], 由于后面减1运算, 跳过0
            for j in range(i, 0, -1):  # [i, i-1, ..., 2, 1], 跳过0, 循环交换, 相当于查找正确的插入位置

                if Q[j] < Q[j - 1]:
                    Q[j], Q[j - 1] = Q[j - 1], Q[j]
                else:  # 提前终止
                    break


if __name__ == '__main__':
    InsertionSort().test()
