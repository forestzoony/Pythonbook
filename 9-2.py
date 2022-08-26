#중복된 문자를 제외하고 사전식 순서로 나열할 것. 
#입력값이 "bcabc"라면, 출력값은 중복값을 제외한 사전식 나열인 "abc"가 될 것이다. 

#방법1) 재귀를 이용하여 분리한다. 
def removeDuplicateLetters(self, s:str)-> str:
    for char in sorted(set(s)):
        suffix=s[s.index(char):]

        if set(s) == self(suffix):
            return char + self.removeDuplicatedLetters(suffix.replace(char,''))
    return ''

#방법2) 스택을 이용하여 문자를 제거한다. 
def removeDuplicateLetters(self, s:str) -> str: 
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s: 
        counter[char] -= 1
        if char in seen: 
            continue
        
        while stack and char < stack[-1] and counter[stack[-1]]> 0:
            seen.remove(stack.pop())
        stack.append(char) 
        seen.add(char)

    return ''.join(stack)