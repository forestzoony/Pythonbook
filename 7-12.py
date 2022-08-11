#한 번의 거래로 낼 수 있는 최대의 이익을 산출할 것. 

#입력 : [7,1,5,3,6,4]
#출력 ; 5

#풀이방법: 브루트 포스로 계산한다. 
def maxProf(self, prices: List[int])-> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price) #최대의 이익을 리턴값으로 담음. 


    return max_price

