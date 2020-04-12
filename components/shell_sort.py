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


class ShellSort(SortTest):
    """ 将数据分组做插入排序，利用了插入排序在少量数据上速度快的优势 """

    def sort(self, Q: list):
        h = 1
        while h < len(Q) // 3:
            h = h * 3 + 1

        while h >= 1:
            for i in range(h, len(Q)):
                for j in range(i, h - 1, -h):
                    if Q[j] < Q[j - h]:
                        Q[j], Q[j - h] = Q[j - h], Q[j]
                    else:
                        break

            h //= 3


if __name__ == '__main__':
    ShellSort().test()
