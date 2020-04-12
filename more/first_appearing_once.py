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
    请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从
    该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

    ord(), char()
    """

    def __init__(self):
        self.cnts = [0 for _ in range(256)]  # 字符转数字的处理方法
        self.que = []

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if not self.que:
            return '#'
        else:
            return self.que[0]

    def Insert(self, char):
        # write code here
        self.cnts[ord(char)] += 1
        if char not in self.que:
            self.que.append(char)
        while self.que and self.cnts[ord(self.que[0])] > 1:
            self.que.pop(0)


if __name__ == '__main__':
    so = Solution()
    [so.Insert(k) for k in "google"]
    print(so.FirstAppearingOnce())
