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


class UglyNumber:
    """
    动态规划问题

    把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑
    数。求按从小到大的顺序的第N个丑数。

    思路：
    由于数组递增，记录三个指针，分别时要乘2的数，要乘3的数，要乘5的数，dp[k]即为上面三个数各自乘之后的最小值
    """

    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        dp = [1 for _ in range(index)]

        u1, u2, u3 = 0, 0, 0  # 三个指针，分别对应2,3,5
        for k in range(1, len(dp)):
            dp[k] = min([dp[u1] * 2, dp[u2] * 3, dp[u3] * 5])  # 取最小值
            if dp[k] == dp[u1] * 2:  # 指针移动
                u1 += 1
            if dp[k] == dp[u2] * 3:
                u2 += 1
            if dp[k] == dp[u3] * 5:
                u3 += 1

        return dp[index - 1]


if __name__ == '__main__':
    ret = UglyNumber().GetUglyNumber_Solution(1500)
    print(ret)
