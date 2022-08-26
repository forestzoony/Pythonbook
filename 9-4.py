#큐를 이용해 다음 연산을 지원하는 스택을 구현할 것. 
#예시) Mystack stack = new Mystack();
      #stack.push(1);
      #stack.push(2);
      #stack.top() // 2리턴
      #stack.pop() // 2리턴
      #stack.empty() // false리턴

#방법1) push()할 때, 큐를 이용해 재정렬할 것.
class Mystack: 
    def __init__(self): 
        self.q = collections.deque()

    def push(self,x):
        self.q.append(x)

        for _ in range(len(self.q))-1:
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

