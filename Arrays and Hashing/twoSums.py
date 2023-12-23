from typing import List


class Solution:
    @staticmethod
    def two_sums(nums: List[int], target: int) -> List[int]:
        indices: dict[int, int] = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in indices:
                return [i, indices[difference]]
            indices[num] = i

        return []


if __name__ == '__main__':
    result1 = Solution.two_sums([11, 7, 2, 15], 9)
    print(result1)

    result2 = Solution.two_sums([3, 2, 4], 6)
    print(result2)

    result3 = Solution.two_sums([3, 3], 6)
    print(result3)
