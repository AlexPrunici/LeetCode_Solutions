from typing import List


class Solution:

    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


if __name__ == '__main__':
    result1 = Solution.contains_duplicate([1, 2, 3, 1])
    print(result1)

    result2 = Solution.contains_duplicate([1, 2, 3, 4])
    print(result2)

    result3 = Solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(result3)
