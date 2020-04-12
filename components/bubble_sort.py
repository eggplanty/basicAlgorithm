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


class BubbleSort:
    """
    冒泡排序, 最少时间复杂度O(n), 最大时间复杂度O(n^2), 在反向有序时达到
    """

    def bubble_sory(self, Q: list):

        for i in range(len(Q) - 1, 0, -1):  # 循环从Q的第n-1个元素到第1个元素,低龄个元素不需要在冒泡了
            is_sorted = True

            for j in range(0, i):  # 从第0个元素到第i-1个
                if Q[j] > Q[j + 1]:  # 冒泡交换
                    Q[j], Q[j + 1] = Q[j + 1], Q[j]
                    is_sorted = False

            if is_sorted:  # 如果没有冒泡，说明已经有序，提前结束
                return


if __name__ == '__main__':
    ls = [5, 4, 3, 2, 6, 76, 43, 6, 1, 3]
    BubbleSort().bubble_sory(ls)
    print(ls)
