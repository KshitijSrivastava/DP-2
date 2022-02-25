## Problem2 (https://leetcode.com/problems/coin-change-2/)


class Solution:
    def change_recur(self, amount, coins, idx):
        if amount == 0:                         #if amount is 0, then one combination is found
            return 1
        elif amount < 0:                        #if amount is less than 0, no combination found
            return 0
        elif idx < 0:                           #if index is less than 0, no combination found
            return 0
        
        #use the coins provided by the index
        take = self.change_recur(amount - coins[idx], coins, idx)
        #Don't use the coin provided and go to a idex less than previous
        not_take = self.change_recur(amount, coins, idx - 1)
            
        #sum the total ways of taking and not taking
        return take + not_take
    
    #memoization
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def change_recur(amount, coins, idx):
            if amount == 0:
                return 1
            elif amount < 0:
                return 0
            elif idx < 0:
                return 0
            elif (amount, idx) in dp:
                return dp[ (amount, idx) ]

            take = change_recur(amount - coins[idx], coins, idx)
            not_take = change_recur(amount, coins, idx - 1)
            dp[(amount, idx)] = take + not_take
            return dp[(amount, idx)]

        return change_recur(amount, coins, len(coins)-1)
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = []
        
        #first row is of zeros
        for i in range(n + 1):
            dp.append([0 for j in range(amount + 1)])
            
        #first column is of ones. (One combination of empty for 0)
        for i in range(n+1):
            dp[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, amount + 1):
                #if amount is greater than the paticular coin
                if j >= coins[i-1]:
                    #take the coin or don't take the coin
                    dp[i][j] = dp[i-1][j] + dp[i][ j - coins[i-1] ]
                else:
                    #if not taken the coin
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amount]