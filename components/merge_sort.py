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


class MergeSort(SortTest):
    """ 归并排序, 先将序列一分为二, 递归分别排序, 结果合并 """

    tmp = []

    def merge(self, Q: list, l: int, m: int, r: int):
        """ 左右指针，将小的值写入 """

        self.tmp = [q for q in Q]
        i, j = l, m + 1

        for k in range(l, r + 1):
            if i > m:
                Q[k] = self.tmp[j]
                j += 1

            elif j > r:
                Q[k] = self.tmp[i]
                i += 1

            elif self.tmp[i] <= self.tmp[j]:  # 保证稳定性
                Q[k] = self.tmp[i]
                i += 1

            else:
                Q[k] = self.tmp[j]
                j += 1

    def rec_sory(self, Q: list, l: int, r: int):
        if r <= l:
            return

        mid = l + (r - l) // 2
        self.rec_sory(Q, l, mid)
        self.rec_sory(Q, mid + 1, r)
        self.merge(Q, l, mid, r)

    def sort(self, Q: list):
        self.rec_sory(Q, 0, len(Q) - 1)


if __name__ == '__main__':
    MergeSort().test()
