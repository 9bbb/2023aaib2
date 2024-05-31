class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        table={}#大括號
        for num in nums:#每個數字倫一次
            if num in table:#每個數字倫一次
                table[num]+=1#次數加一
            else:
                table[num]=1#第一次出現
        #print(table)
        ans=0
        for num in table:
            if table[num] ==2:
                ans=ans ^ num

        return ans