#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/3/30
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------


class QuickSort:
    """
    快速排序, 通过选定基准值, 将序列分为比基准值小和比基准值大, 递归即可得到排序队列
    在队列反向有序时, 排序数深度会等于队列长度，即都在一棵树上, 这时
    """

    def quick_sort(self, Q: list, a: int, b: int):
        """ Q待排序队列, a左边index, b右边index """

        if a > b:
            return

        # r必须是b-1，不能是b，在计算时不能将基准点纳入，否则l>r时会超出边界
        l, r, p = a, b - 1, Q[b]  # left, right, pivot

        while l <= r:
            while l <= r and Q[l] < p:  # 找到第一个不应该在基准值左边的index
                l += 1
            while l <= r and p < Q[r]:  # 找到第一个不应该在基准值右边的index
                r -= 1

            if l <= r:
                Q[l], Q[r] = Q[r], Q[l]  # 交换基准值两边不正确的位置的值
                l, r = l + 1, r - 1

        Q[l], Q[b] = Q[b], Q[l]  # l位置的值大于等于基准值, 将l位置的值与基准值互换
        self.quick_sort(Q, a, l - 1)
        self.quick_sort(Q, l + 1, b)


if __name__ == '__main__':
    ls = [5, 4, 3, 2, 6, 76, 43, 6, 1, 3]
    QuickSort().quick_sort(ls, 0, len(ls) - 1)
    print(ls)
