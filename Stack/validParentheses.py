class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        bracket_map = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in bracket_map.keys():
                stack.append(c)
            elif c in bracket_map.values():
                if len(stack) == 0 or bracket_map[stack.pop()] != c:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    result1 = Solution.is_valid("()")
    print(result1)

    result2 = Solution.is_valid("()[]{}")
    print(result2)

    result3 = Solution.is_valid("(]")
    print(result3)
