#스택을 이용하여 다음 연산을 지원하는 큐를 구현할 것. 

#MyQueue queue = new Myqueue();
 #queue.push(1);
 #queue.push(2);
 #queue.peek(); // 1리턴
 #queue.pop(); // 1리턴 
 #queue.empty // false

 #방법1) 스택 2개 사용하기 
  class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
    
    def push(self,x):
        self.input.append(x)
    
    def pop(self): 
        self.peek()
        return self.output.pop()

    def peek(self): 
        if not self.output():
            while self.input:
                self.output.append(self.input.pop())
        return self.append[-1]

    def empty(self): 
        return self.input == [] and self.output == []

