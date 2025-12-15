from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# It takes the raw input (List[int]) and returns the format needed for the solution (TreeNode)
def list_to_tree(data: List[int]) -> Optional[ListNode]:
    if not data:
        return None
    
    root = ListNode(data[0])
    current = root

    for val in data[1:]:
        current.next = ListNode(val)
        current = current.next

    return root

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        last_odd_node = head
        last_even_node = head.next
        start_even_nodes = head.next
        next_odd_node = last_even_node.next
        next_even_node = next_odd_node.next if next_odd_node else None

        while next_odd_node != None and next_even_node != None:
            last_odd_node.next = next_odd_node
            last_even_node.next = next_even_node

            last_odd_node = next_odd_node
            last_even_node = next_even_node

            next_odd_node = next_even_node.next
            next_even_node = next_odd_node.next if next_odd_node else None
        
        if next_odd_node != None:
            last_odd_node.next = next_odd_node
            last_odd_node = next_odd_node
        
        last_odd_node.next = start_even_nodes
        # otherwhise this could point to lon and we end up with a loop
        last_even_node.next = None
        return head

SOLUTIONS = {
    "tree_approach": Solution().oddEvenList,
}

SETUPS = {
    "tree_approach": list_to_tree,
}