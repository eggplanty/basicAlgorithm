#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/7
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------


class InversePairs:
    """
    巧妙使用归并排序

    数组中的逆序对
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并
    将P对1000000007取模的结果输出。 即输出P%1000000007
    """

    def __init__(self):
        self.cnt = 0

    def merge(self, ls, l, m, r):

        i, j = l, m + 1
        tmp = [q for q in ls]

        for k in range(l, r + 1):
            if i > m:
                ls[k] = tmp[j]
                j += 1
            elif j > r:
                ls[k] = tmp[i]
                i += 1
            elif tmp[i] <= tmp[j]:
                ls[k] = tmp[i]
                i += 1
            else:
                ls[k] = tmp[j]
                j += 1
                self.cnt += m - i + 1  # 有归并排序可知，如果tmp[i]>tmp[j], 则tmp[i,...,m] > tmp[j]

    def recur(self, ls, l, r):
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.recur(ls, l, mid)
        self.recur(ls, mid + 1, r)
        self.merge(ls, l, mid, r)

    def InversePairs(self, data):
        # write code here
        self.recur(data, 0, len(data) - 1)
        return self.cnt % 100000000007


if __name__ == '__main__':
    ret = InversePairs().InversePairs([1, 2, 3, 4, 5, 6, 7, 0])
    print(ret)

    ret = InversePairs().InversePairs(
        [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575])
    print(ret)
