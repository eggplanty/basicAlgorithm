#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/4
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------
from components.sort_test import SortTest


class T(SortTest):
    """ 选择排序 """

    def sort(self, Q: list):
        for i in range(0, len(Q)):
            for j in range(i, len(Q)):
                if Q[i] > Q[j]:
                    Q[i], Q[j] = Q[j], Q[i]


class T2(SortTest):
    """ 冒泡排序 """

    def sort(self, Q: list):
        for i in range(len(Q) - 1, 0, -1):
            is_sorted = True
            for j in range(0, i):
                if Q[j] > Q[j + 1]:
                    Q[j], Q[j + 1] = Q[j + 1], Q[j]
                    is_sorted = False
            if is_sorted:
                break


class T3(SortTest):
    """ 插入排序 """

    def sort(self, Q: list):
        for i in range(1, len(Q)):
            for j in range(i, 0, -1):
                if Q[j - 1] > Q[j]:
                    Q[j - 1], Q[j] = Q[j], Q[j - 1]
                else:
                    break


class T4(SortTest):
    """ 归并排序 """

    def merge(self, Q: list, l: int, m: int, r: int):
        tmp = [q for q in Q]
        i, j = l, m + 1

        for k in range(l, r + 1):
            if i > m:
                Q[k] = tmp[j]
                j += 1
            elif j > r:
                Q[k] = tmp[i]
                i += 1
            elif tmp[i] <= tmp[j]:
                Q[k] = tmp[i]
                i += 1
            else:
                Q[k] = tmp[j]
                j += 1

    def recur(self, Q: list, l: int, r: int):
        if l >= r:
            return

        mid = l + (r - l) // 2
        self.recur(Q, l, mid)
        self.recur(Q, mid + 1, r)
        self.merge(Q, l, mid, r)

    def sort(self, Q: list):
        self.recur(Q, 0, len(Q) - 1)


class T5(SortTest):
    """ 希尔排序 """

    def sort(self, Q: list):
        h = 1
        while h < len(Q) // 3:
            h = 3 * h + 1  # 1, 4, 10,...

        while h >= 1:
            for i in range(h, len(Q)):
                for j in range(i, h - 1, -1):
                    if Q[j - h] > Q[j]:
                        Q[j - h], Q[j] = Q[j], Q[j - h]
                    else:
                        break
            h //= 3


class T6(SortTest):
    """ 快速排序 """

    def recur(self, Q: list, l: int, r: int):
        if l > r:
            return
        i, j, p = l, r - 1, Q[r]
        while i <= j:
            while i <= j and Q[i] < p:
                i += 1

            while i <= j and Q[j] > p:
                j -= 1

            if i <= j:
                Q[i], Q[j] = Q[j], Q[i]
                i += 1
                j -= 1

        Q[i], Q[r] = Q[r], Q[i]
        self.recur(Q, l, i - 1)
        self.recur(Q, i + 1, r)

    def sort(self, Q: list):
        self.recur(Q, 0, len(Q) - 1)


class T7(SortTest):
    """ 堆排序 """

    def sink(self, Q: list, k: int, n: int):
        while 2 * k <= n:
            j = 2 * k
            if j < n and Q[j + 1] > Q[j]:
                j += 1
            if Q[j] < Q[k]:
                break
            Q[j], Q[k] = Q[k], Q[j]
            k = j

    def sort(self, Q: list):
        Q.insert(0, 0)

        N = len(Q) - 1
        for k in range(N // 2, 0, -1):
            self.sink(Q, k, N)

        for k in range(N, 0, -1):
            Q[1], Q[k] = Q[k], Q[1]
            self.sink(Q, 1, k - 1)

        Q.pop(0)


if __name__ == '__main__':
    T7().test()
