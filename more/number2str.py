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


class Solution:
    """
    非波那契数列变种

    给定一个数字，按照如下规则翻译成字符串：1 翻译成“a”，2 翻译成“b”... 26 翻译成“z”。一个数字有多种翻译可能，例如 12258 一共有 5 种，
    分别是 abbeh，lbeh，aveh，abyh，lyh。实现一个函数，用来计算一个数字有多少种不同的翻译方法。

    """

    def num2char(self, num):
        return 1 if int(num) > 0 and int(num) < 27 else 0

    def test(self, str):
        if len(str) == 0:
            return 0
        elif len(str) == 1:
            return 1
        elif len(str) == 2:
            return 1 + self.num2char(str[0:2])

        c_2, c_1 = 1, 1 + self.num2char(str[0:2])
        for k in range(2, len(str)):

            if self.num2char(str[k - 1:k + 1]) > 0:  # 如果两步可达，则是正常的非波那契数列问题
                c_1, c_2 = c_1 + c_2, c_1
            else:
                c_1 = c_1  # 如果两步不可达，则c_1不变
                c_2 = c_1

        return c_1


if __name__ == '__main__':

    ret = Solution().test('12258')
    print(ret)
