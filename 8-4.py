#역순으로 저장된 연결 리스트의 숫자를 더할 것. 
#입력) (2-> 4-> 3) + (5-> 6-> 4) 출력) 7-> 0-> 8

#풀이방법: 모든 수를 역순한 후, 더하면 값이 나오는데 그 값도 역순으로 출력하면 된다. 

#풀이1) 자료형 변환
from typing import List


class Solution: 
    def reverseList(self, head: ListNode) -> ListNode:
        node,prev = head, None

        while node: 
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self,node: ListNode)-> List: 
        list: List=[]
        while node:
            list.append(node.val)
            node = node.next
        return List

