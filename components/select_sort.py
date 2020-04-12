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


class SelectSort(SortTest):

    def sort(self, Q: list):
        for i in range(0, len(Q) - 1):
            for j in range(i, len(Q)):
                if Q[j] < Q[i]:
                    Q[j], Q[i] = Q[i], Q[j]


if __name__ == '__main__':
    SelectSort().test()
