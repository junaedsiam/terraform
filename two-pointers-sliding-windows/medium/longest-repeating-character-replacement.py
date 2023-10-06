"""
Problem description: 
---------

"""


def longest_repeating_character_replacement(s: str, k: int):
    # Maintain a frequency count of letter
    # two pointers to track the length of the substring and sliding
    l = 0
    max_len = 0
    freq = {}

    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1

        curr_len = r - l + 1

        if curr_len - max(freq.values()) <= k:
            max_len = max(max_len, curr_len)
        else:
            freq[s[l]] -= 1
            l += 1

    return max_len


if __name__ == '__main__':
    print(longest_repeating_character_replacement("ABAB", 2))
    print(longest_repeating_character_replacement("AABABBA", 1))
