#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/8
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 阿里笔试实例
# @Reference   : 
# ----------------------------------
import sys


class Test:
    """


    题目是说要打怪兽（一个箭打一个怪兽，打死这一个打下一个，都打完了就计算付出的代价，每支箭都有对应的代价，输出加和最小的那个，打不死就
    凉了（输出“No”）），用例的第一个数字表示测试数据的组数（两组），然后分别输入这几（两）组

    测试用例
    2
    3 3
    1 2 3
    2 3 4
    1 2 3
    3 4
    1 2 3
    1 2 3 4
    1 2 3 1

    """

    def line2list(self, line: str, f=int, sp=' '):
        """ 将一个字符串去处左右空格, 按照sp分割, 并对每个分割单元执行f方法 """
        l_ls = line.strip().split(sp)
        return list(map(f, l_ls))

    def test(self):
        n = int(sys.stdin.readline().strip())
        for i in range(n):
            cnt_ls = self.line2list(sys.stdin.readline())
            monster = self.line2list(sys.stdin.readline())
            arror = self.line2list(sys.stdin.readline())
            cost = self.line2list(sys.stdin.readline())
            print(cnt_ls, monster, arror, cost)
            print('-' * 10)


if __name__ == '__main__':
    Test().test()
