class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        T = [0]*101 #統計數字出現次數 1...100 所以要開101個
        best = 0
        for num in nums:
            T[num] +=1
            if T[num] > best:best = T[num]
        #到這裡 T就有全部的數字出現的次數了 且best就是最多的數字
        #把全部最多的都加起來
        total = 0
        for t in T:
            if t==best: total += t
        return total