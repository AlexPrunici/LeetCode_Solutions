import re


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        filtered_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        if not filtered_string.strip():
            return True

        return filtered_string == filtered_string[::-1] if filtered_string else False


if __name__ == '__main__':
    result1 = Solution.is_palindrome("A man, a plan, a canal: Panama")
    print(result1)

    result2 = Solution.is_palindrome("race a car")
    print(result2)

    result3 = Solution.is_palindrome(" ")
    print(result3)
