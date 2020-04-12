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


class SortTest:
    def __init__(self):
        self.__test_cases = [
            [],
            [1, 2, 3],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 6, 76, 43, 6, 1, 3],
            [3, 6, 87, 43, 76, 0, 43, 56, 4, 67, 56, 77, 88, 65]
        ]

        self.__answer = [
            [],
            [1, 2, 3],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 3, 4, 5, 6, 6, 43, 76],
            [0, 3, 4, 6, 43, 43, 56, 56, 65, 67, 76, 77, 87, 88]
        ]

    def sort(self, Q: list):
        pass

    def __match(self, a, b):
        if len(a) != len(b):
            return False

        for k in range(len(a)):
            if a[k] != b[k]:
                return False

        return True

    def test(self):
        for k, q in enumerate(self.__test_cases):
            print(f"原始队列: {q}.")
            self.sort(q)
            result = "正确" if self.__match(q, self.__answer[k]) else "X"
            print(f"排序队列: {q}.")
            print(f"<<<{result}>>>\n")
