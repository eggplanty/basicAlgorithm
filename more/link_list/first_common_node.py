#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/8
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 
# @Reference   : 
# ----------------------------------


class CommonNode:
    """
    链表经常是通过循环来处理一些特殊问题

    找两个链表的第一个公共节点
    输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

    思路：
    设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
    当访问链表 A 的指针访问到链表尾部时，令它从链表 B 的头部重新开始访问链表 B；同样地，当访问链表 B 的指针访问到链表尾部时，令它从链
    表 A 的头部重新开始访问链表 A。这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。

    """

    def FindFirstCommonNode(self, pHead1, pHead2):
        p1, p2 = pHead1, pHead2
        while pHead1 != pHead2:
            pHead1 = pHead1.next if pHead1 else p2
            pHead2 = pHead2.next if pHead2 else p1

        return pHead1
