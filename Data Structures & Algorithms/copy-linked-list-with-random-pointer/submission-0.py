"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #on recrée une copie de chaque node sans les liens ensuite on reassigne les pointeurs dans une deuxieme boucle

        Map = {None: None}

        cur  = head
        while cur:
            copynode = Node(cur.val)
            Map[cur] = copynode
            cur = cur.next

        cur = head

        while cur:
            copynode = Map[cur]
            copynode.next = Map[cur.next]
            copynode.random = Map[cur.random]
            cur = cur.next

        return Map[head]
        