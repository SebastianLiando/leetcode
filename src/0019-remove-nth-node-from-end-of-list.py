# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = {}

        # Iterate to match index with list node and get size
        tmp = head
        i = 0

        while not tmp == None:
            nodes[i] = tmp
            tmp = tmp.next
            i += 1
        
        # Get the index to remove
        index_to_remove = i - n

        # Connect the node before the index with the node after the index
        # get() will return none if key is out of index
        before = nodes.get(index_to_remove - 1)
        after = nodes.get(index_to_remove + 1) 

        if before == None and after == None:
            # Handle only 1 element
            return None
        if before == None:
            # Handle the case when the index to remove is 0
            return nodes[1]
        else:
            before.next = after
            return head
    
def python_list_to_list_node(python_list):
    res_head = ListNode(python_list[0])
    res = res_head

    for i in range(1, len(python_list)):
        res.next = ListNode(python_list[i])
        res = res.next

    return res_head

def list_node_to_python_list(list_node):
    res = []
    tmp = list_node

    while not tmp == None:
        res.append(tmp.val)
        tmp = tmp.next
        
    return res

def get_result_from_solution(list, n):
    list_node = python_list_to_list_node(list)
    return list_node_to_python_list(Solution().removeNthFromEnd(list_node, n))

def test_case_1():
    assert get_result_from_solution([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]

def test_case_2():
    assert get_result_from_solution([1], 1) == []

def test_case_remove_first():
    assert get_result_from_solution([1, 2, 3, 4, 5], 5) == [2, 3, 4, 5]

def test_case_remove_last():
    assert get_result_from_solution([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4]