class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [-1] * (amount + 1)

        change[0] = 0
        for coin in sorted(coins):
            if coin > amount + 1:
                break

            for c in range(coin, amount+1):
                if change[c-coin] == -1:
                    continue
                change[c] = min(change[c], change[c-coin]+1) if change[c] != -1 else change[c-coin]+1

        return change[amount]
