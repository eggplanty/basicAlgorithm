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


class T(SortTest):

    def sort(self, Q: list):
        for i in range(0, len(Q) - 1):
            for j in range(i, len(Q)):
                if Q[j] < Q[i]:
                    Q[j], Q[i] = Q[i], Q[j]


class T2(SortTest):

    def sort(self, Q: list):

        for i in range(len(Q) - 1, 0, -1):
            is_sorted = True

            for j in range(0, i):
                if Q[j + 1] < Q[j]:
                    Q[j + 1], Q[j] = Q[j], Q[j + 1]
                    is_sorted = False

            if is_sorted:
                break


class T3(SortTest):

    def sort(self, Q: list):
        for i in range(1, len(Q)):
            for j in range(i, 0, -1):
                if Q[j] < Q[j - 1]:
                    Q[j], Q[j - 1] = Q[j - 1], Q[j]
                else:
                    break


class T4(SortTest):

    def sort(self, Q: list):
        h = 1
        while h < len(Q) // 3:
            h = h * 3 + 1

        while h >= 1:
            for i in range(h, len(Q)):
                for j in range(i, h - 1, -h):
                    if Q[j] < Q[j - h]:
                        Q[j], Q[j - h] = Q[j - h], Q[j]
            h //= 3


if __name__ == '__main__':
    T4().test()
