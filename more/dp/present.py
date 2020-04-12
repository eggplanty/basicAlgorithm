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


class Present:
    """
    动态规划问题
    在一个 m*n 的棋盘的每一个格都放有一个礼物，每个礼物都有一定价值（大于 0）。从左上角开始拿礼物，每次向右或向下移动一格，直到右下角
    结束。给定一个棋盘，求拿到礼物的最大价值。例如，对于如下棋盘
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]

    做烂了的路径dp问题 万变不离其宗
    当前点的最大总价值 = max(上面点最大总价值，左边点的最大总价值) + 当前点价值
    (0, 0)点以及第一行和第一列要先初始化一波
    """
    def test(self, LL):
        if not LL or len(LL) <= 0 or len(LL[0]) <= 0:
            return 0

        dp = [[0 for _ in l] for l in LL]
        m, n = len(LL), len(LL[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[0][0] = LL[0][0]
                elif i == 0:  # 第一行初始化
                    dp[i][j] = dp[i][j - 1] + LL[i][j]
                elif j == 0:  # 第一列初始化
                    dp[i][j] = dp[i - 1][j] + LL[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + LL[i][j]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    LL = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]
    ]
    ret = Present().test(LL)
    print(ret)
