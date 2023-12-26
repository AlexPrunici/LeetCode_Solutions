from typing import List
from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        if not prices:
            return 0

        buy_index: int = 0
        sell_index: int = 1
        max_profit: int = 0

        while sell_index < len(prices):
            if prices[buy_index] < prices[sell_index]:
                profit = prices[sell_index] - prices[buy_index]
                max_profit = max(profit, max_profit)
            else:
                buy_index = sell_index
            sell_index += 1

        return max_profit


if __name__ == '__main__':
    result1 = Solution.max_profit([7, 1, 5, 3, 6, 4])
    print(result1)

    result2 = Solution.max_profit([7, 6, 4, 3, 1])
    print(result2)
