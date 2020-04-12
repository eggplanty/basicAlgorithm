#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ----------------------------------
# @Date        : 2020/4/10
# @Author      : Zhicheng Qian
# @Version     : 1.0 
# @Brief       : 
# @Description : 反转链表
# @Reference   : 
# ----------------------------------


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    反转链表
    输入一个链表，反转链表后，输出新链表的表头。

    主要有两种方法，迭代法和递归法
    迭代法为设置一个头指针，不断先头指针后面添加即可

    递归法：返回新的头，在其中，原当前节点的下一个节点的下一个节点改成了当前节点
    """

    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        new = self.ReverseList(pHead.next)  # 输入下一个节点，获得反转后的根节点
        nt = pHead.next
        pHead.next = None  # 将当前节点的下一个节点置为空
        nt.next = pHead  # 将当前节点挂在到反转链的末尾
        return new


if __name__ == '__main__':
    node_ls = [ListNode(i) for i in range(10)]
    for k in range(len(node_ls) - 1):
        node_ls[k].next = node_ls[k + 1]

    ret = Solution().ReverseList(node_ls[0])
    while ret:
        print(ret.val)
        ret = ret.next
