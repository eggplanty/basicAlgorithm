#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/6
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------


class BMA:
    """
    from cyc2018
    多数投票问题，可以利用 Boyer-Moore Majority Vote Algorithm 来解决这个问题，使得时间复杂度为 O(N)。

    使用 cnt 来统计一个元素出现的次数，当遍历到的元素和统计元素相等时，令 cnt++，否则令 cnt--。如果前面查找了 i 个元素，且 cnt == 0，
    说明前 i 个元素没有 majority，或者有 majority，但是出现的次数少于 i / 2 ，因为如果多于 i / 2 的话 cnt 就一定不会为 0 。此时剩下
    的 n - i 个元素中，majority 的数目依然多于 (n - i) / 2，因此继续查找就能找出 majority。
    """

    def more_than_half_of_nums(self, numbers):
        """ 找出numbers中出现次数超过一半的值, 如果不存在则返回0(包括等于一半)  """

        if not numbers:
            return 0

        cnt, maj = 1, numbers[0]
        for i in range(1, len(numbers)):  # 第一次循环找到可能的多数值
            cnt = cnt + 1 if numbers[i] == maj else cnt - 1
            if cnt == 0:
                cnt, maj = 1, numbers[i]

        cnt = 0
        for i in range(0, len(numbers)):
            cnt = cnt + 1 if numbers[i] == maj else cnt

        return maj if cnt > len(numbers) // 2 else 0
