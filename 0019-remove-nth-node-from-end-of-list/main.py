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
    