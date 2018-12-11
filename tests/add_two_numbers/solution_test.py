import sys
sys.path.insert(0, "../../src/add_two_numbers")

try:
    from solution import Solution, ListNode
    # from list_node import ListNode
except ImportError:
    print('No Import')

def test_answer():
    expectedAnswer = [2, 0, 6]
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

    assert(len(expectedAnswer) == len(answer) and sorted(expectedAnswer) == sorted(answer))    