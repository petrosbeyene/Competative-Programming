class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev = self.getRow(rowIndex-1)
        ans = [1]*(rowIndex+1)
        for i in range(1, len(ans)-1):
            ans[i] = prev[i-1]+prev[i]
        
        return ans
        
