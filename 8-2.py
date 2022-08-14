#정렬되어 있는 두 연결리스트를 합칠 것
#입력) 1->2->4 , 1->3->4
#츨력) 1->1->2->3->4->4

#풀이방법: 숫자를 크기순으로 나열하고, 이를 출력하면 된다. 

#방법1) 재귀 구조로 연결하기 
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if(not l1) or (l2 and l1.val > l2.val):
        l1,l2 = l2,l1
    if l1:
        l1.next = self.mergeTwoLists(l1,next, l2)
    return l1

