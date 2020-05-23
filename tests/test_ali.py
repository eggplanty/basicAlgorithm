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


class T:
    def __init__(self, LL):
        self.dp = [[-1] * len(l) for l in LL]

    def recur(self, LL, i, j, n):
        if j == n:
            self.dp[i][j] = 0
            return self.dp[i][j]

        dp0 = self.dp[0][j + 1] if self.dp[0][j + 1] > 0 else self.recur(LL, 0, j + 1, n)
        dp1 = self.dp[1][j + 1] if self.dp[1][j + 1] > 0 else self.recur(LL, 1, j + 1, n)
        dp2 = self.dp[2][j + 1] if self.dp[2][j + 1] > 0 else self.recur(LL, 2, j + 1, n)

        self.dp[i][j] = min(
            [
                dp0 + abs(LL[0][j + 1] - LL[i][j]),
                dp1 + abs(LL[1][j + 1] - LL[i][j]),
                dp2 + abs(LL[2][j + 1] - LL[i][j]),
            ])

        return self.dp[i][j]

    def test(self, LL):
        n = len(LL[0]) - 1
        return min([self.recur(LL, 0, 0, n), self.recur(LL, 1, 0, n), self.recur(LL, 2, 0, n)])


if __name__ == '__main__':
    # LL = [[1, 3, 6], [2, 4, 7], [3, 5, 10]]
    LL = [[1, 6, 12], [2, 8, 20], [3, 9, 30]]

    tt = T(LL)
    ret = tt.test(LL)
    print(ret)
