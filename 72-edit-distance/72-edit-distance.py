class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1)+ 1)]

        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1)-i
        
        for j in range(len(word2)):
            dp[len(word1)][j] = len(word2)-j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = 0 + dp[i+1][j+1]
                else:
                    # 1 + dp[i][j+1] --> Insert Operation
                    # 1 + dp[i+1][j] --> Remove/Ignore Operation
                    # 1 + dp[i+1][j+1] --> Replace Operation 
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]
