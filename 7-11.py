#배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력할 것.
#입력)[1,2,3,4],출력)[24,12,8,6]

#풀이방법: 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱한다. 

def productExcepetSelf(self,nums: List[int]) -> List[int]:
    output = []

    p = 1

    for i in range(0,len(num)):
        output.append(p)
        p = p * num[i]

    p = 1

    for i in range(len(nums) -1, 0-1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return output