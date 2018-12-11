# from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        condition = True

        l3 = ListNode(0)
        l3_head = l3

        while condition:
            total = l1.val + l2.val + carry
            placeVal = total - 10 if total > 9 else total
            carry = 1 if total > 9 else 0

            l3.val = placeVal

            condition = True if l1.next is not None else False
            if condition:
                l1 = l1.next
                l2 = l2.next
                l3.next = ListNode(0)
                l3 = l3.next

        return l3_head

if __name__ == '__main__':
    # [5, 7, 4]
    l1 = ListNode(5)
    l1_head = l1

    l1.next = ListNode(7)
    l1 = l1.next
    l1.next = ListNode(4)

    # [7, 2, 1]
    l2 = ListNode(7)
    l2_head = l2

    l2.next = ListNode(2)
    l2 = l2.next
    l2.next = ListNode(1)

    sn = Solution()
    ret_list_node = sn.addTwoNumbers(l1_head, l2_head)

    answer = [ret_list_node.val]
    while ret_list_node.next is not None:
        answer.append(ret_list_node.next.val)
        ret_list_node = ret_list_node.next

    print(answer)
