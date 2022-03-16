from LeeCode.LinkedListQues import ListNode


def delete_node(head: ListNode, val: int) -> ListNode:
    """
    Offer 18. 删除链表的节点
    :param head:
    :param val:
    :return:
    """
    virtual = ListNode(0)
    virtual.next = head
    pre, cur = virtual, head
    while cur:
        if cur.val == val:
            pre.next = cur.next
            break
        else:
            pre, cur = cur, cur.next
    return virtual.next


def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    """
    Offer 22. 链表中的倒数第 K 个节点
    :param head:
    :param k:
    :return:
    """
    left = head
    for _ in range(k):
        head = head.next
    right = head
    while right:
        left, right = left.next, right.next
    return left


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Offer 25. 合并两个排序的链表
    :param l1:
    :param l2:
    :return:
    """
    virtual = ListNode(0)
    cur = virtual
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2

    return virtual.next


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA
    return nodeA
