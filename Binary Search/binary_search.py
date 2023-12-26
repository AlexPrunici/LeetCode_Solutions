from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if nums[middle_index] > target:
                right_index = middle_index - 1
            elif nums[middle_index] < target:
                left_index = middle_index + 1
            else:
                return middle_index

        return -1


if __name__ == '__main__':
    result1 = Solution.search([-1, 0, 3, 5, 9, 12], 9)
    print(result1)

    result2 = Solution.search([-1, 0, 3, 5, 9, 12], 2)
    print(result2)
