class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        print(s)
        return True


if __name__ == '__main__':
    result1 = Solution.is_valid("()")
    print(result1)

    result2 = Solution.is_valid("()[]{}")
    print(result2)

    result3 = Solution.is_valid("(]")
    print(result3)
