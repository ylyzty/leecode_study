# from CodeCatalog.LinkedListQues.ListNode import *

from ListNode import *
"""
代码随想录: 链表部分
"""


class RemoveElement:
    """
    LeeCode 203: 移除链表元素
    """

    def solution(self, head: ListNode, val: int) -> ListNode:
        virtual_head = ListNode(val=0, next=head)
        pre, cur = virtual_head, head

        while not (cur is None):
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return virtual_head.next


class MyLinkedList:
    """
    LeeCode 707: 设计链表, 单向链表
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, None)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val, None)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            print("Add: Index out of range!")
            return

        if index == self.size:
            self.addAtTail(val)
            return

        if index <= 0:
            self.addAtHead(val)
            return

        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        cur = pre.next

        # 插入Node
        node = ListNode(val, None)
        pre.next = node
        node.next = cur

        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            print("Delete: Index out of range!\n")
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        cur = pre.next

        # 删除cur节点
        pre.next = cur.next
        self.size -= 1
        return


class ReverseList:
    """
    LeeCode 206: 翻转链表
    """

    def solution(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        previous, current = head, head.next
        previous.next = None
        while current:
            temp = current.next
            current.next = previous

            # 更新 previous, current节点
            previous = current
            current = temp
        return previous


class SwapPairs:
    """
    LeeCode 24: 两两交换链表中的节点
    """

    def solution(self, head: ListNode) -> ListNode:
        virtual_head = ListNode(0, head)
        previous, current = virtual_head, head
        while current and current.next:
            following = current.next

            # 交换两个相邻节点
            previous.next = following
            current.next = following.next
            following.next = current

            # 更新previous, current
            previous = current
            current = current.next
        return virtual_head.next


class RemoveNthFromEnd:
    """
    LeeCode 19: 删除链表的倒数第 n 个节点
    """

    def solution(self, head: ListNode, n: int) -> ListNode:
        virtualHead = ListNode(0, head)
        slow, fast = virtualHead, virtualHead

        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return virtualHead.next


class GetIntersectionNode:
    """
    LeeCode: 链表相交
    headA 链表长度为 a, headB 链表长度为 b, 链表相交长度为 c

    遍历完 headA 再遍历 headB, 到公共节点, 共经过 a + (b - c + 1) 个节点
    遍历完 headB 再遍历 headA, 到公共节点, 共经过 b + (a - c + 1) 个节点

    - 若 c = 0, 即不存在公共节点, 则当前节点指向 None
    - 若 c > 0, 即存在公共节点, 则当前节点指向公共链表的第一个节点
    """

    def solution(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


class DetectCycle:
    """
    LeeCode 142: 环形链表 II
    设 链表头部到环之前有 a 个节点, 链表环内有 b 个节点
    定义快慢指针 fast, slow, fast每次走两步, slow每次走一步
    - 若 fast 走到链表尾部, 则说明链表无环 return None
    - 若 fast 与 slow 相遇, 则 fast = 2 * slow 且 fast - slow = n * b
    即 fast = 2 * n * b, slow = n * b

    slow 指针走到链表环第一个节点时步数表达式: a + n * b
    所以 slow 指针再走 a 步即到达链表环第一个节点

    如何确定 a 呢 ?
    将指针 fast 重新指向 head, head 走 a 步也到达链表环第一个节点
    即同时移动 fast 和 slow 直至其第二次相遇
    """
    def solution(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast


def printLinkedList(head: ListNode):
    print(f"Current LinkedList is: ", end="")
    node = head
    while node:
        print(node.val, end="")
        if node.next:
            print(" -> ", end="")
        else:
            print("\n", end="")
        node = node.next


"""
测试代码
"""
if __name__ == "__main__":

    node1 = ListNode(3, None)
    node2 = ListNode(2, None)
    node3 = ListNode(0, None)
    node4 = ListNode(4, None)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    delteCyclt.solution(node1)
