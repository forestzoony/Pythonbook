#연결 리스트가 팰린드롬 구조인지 판별할 것

#입력) 1->2 : false
#입력2) 1->2->2->1 : true

#팰린드롬이란 거꾸로 배열을 바꾸어도 대칭을 이루는 것을 말함. 

#풀이방법1) 리스트로 변환한다. (각 엘리먼트를 리스트의 요소로 변환하여 리스트의 형태로 문제를 해결함.)
def isPallindrome(self, head: ListNode) -> bool: 
    q : List = [] 

    if not head:
        return true

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    
    while len(q) > 1: 
        if q.pop(0) != q.pop(): #리스트의 첫번째 요소를 삭제하는 것과 마지막 요소를 삭제하는 것이 같지 않다면
            return False

    return True

 #풀이방법2) 데크를 활용한다. 
 #풀이방법3) 고를 이용하여 데크를 구현한다. 

 