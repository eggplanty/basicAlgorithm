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


class MinNumber:
    """
    把数组排成最小的数
    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组 {3，32，321}，则打印出这
    三个数字能排成的最小数字为 321323。

    排序的本质在于比较与交换, 不局限于数字, 任何可以比较和交换的东西都可以排序
    """

    def is_bigger(self, a, b):
        if int(f"{a}{b}") > int(f"{b}{a}"):
            return True
        else:
            return False

    def PrintMinNumber(self, numbers):
        for i in range(1, len(numbers)):
            for j in range(i, 0, -1):
                if self.is_bigger(numbers[j - 1], numbers[j]):
                    numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
                else:
                    break
        return int(''.join([str(n) for n in numbers]))


if __name__ == '__main__':
    ret = MinNumber().PrintMinNumber([32, 5, 1, 4, 2])
    print(ret)
