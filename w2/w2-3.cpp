class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        one = 0 # s裡面, 有幾個1? 
        for c in s :
            if c=='1':one += 1
        return'1'*(one-1)+'0'*(N-one) + '1'