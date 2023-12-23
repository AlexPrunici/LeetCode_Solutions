class Solution:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = string_to_dict(s)
        t_dict = string_to_dict(t)

        for c in s_dict:
            if s_dict[c] != t_dict.get(c, 0):
                return False

        return True


def string_to_dict(s: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}

    for letter in s:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1

    return char_dict


if __name__ == '__main__':
    result1 = Solution.is_anagram("anagram", "nagaram")
    print(result1)

    result2 = Solution.is_anagram("rat", "car")
    print(result2)
