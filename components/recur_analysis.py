#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/3/23
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------

class RecurAnalysis:
    """
    递归的性能分析，非波那契数列例子
    二分递归: 时间开销O(log2**n)，进行了很多重复计算
    线性递归: 时间开销O(logn)
    """

    def bad_fibonacci(self, n: int) -> int:
        """ 带重复计算的递归 """

        if n <= 1:
            return n

        return self.bad_fibonacci(n - 2) + self.bad_fibonacci(n - 1)

    def good_fibonacci(self, n: int) -> list:
        """ 不进行重复计算 """
        if n <= 1:
            return [n, 0]

        a, b = self.good_fibonacci(n - 1)
        return [a + b, a]


if __name__ == '__main__':
    import time

    ra = RecurAnalysis()
    st_t = time.time()
    print(ra.bad_fibonacci(30))
    print(f"cost {time.time() - st_t}")
    st_t = time.time()
    print(ra.good_fibonacci(30))
    print(f"cost {time.time() - st_t}")
