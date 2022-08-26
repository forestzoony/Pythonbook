#매일의 화씨 온도 리스트를 입력받아서, 더 따뜻한 날시를 위해서는 며칠을 더 기다려야 하는지를 출력할 것. 
#입력) 73,74,75,71,69,72,76,73 -> 출력) 1,1,4,2,1,1,0,0

#풀이1) 스택 값을 비교한다. 
def dailyTemperatures(self, T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append()

    return answer