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
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    printLinkedList(linkedList.head)

    linkedList.addAtTail(3)
    printLinkedList(linkedList.head)

    linkedList.addAtIndex(1, 2)
    printLinkedList(linkedList.head)

    print(linkedList.get(1))
    printLinkedList(linkedList.head)

    linkedList.deleteAtIndex(1)
    printLinkedList(linkedList.head)

    print(linkedList.get(1))
    printLinkedList(linkedList.head)

    node1 = ListNode(1, None)
    node2 = ListNode(2, None)
    node3 = ListNode(3, None)
    node4 = ListNode(4, None)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    swapPais = SwapPairs()
    swapPais.solution(node1)
