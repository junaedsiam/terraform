def is_string_palindrome(str, start, end):
    if start >= end or (start < end and str[start] == str[end] and
                        is_string_palindrome(str, start + 1, end - 1)):
        return True
    return False


if __name__ == '__main__':
    str1, str2, str3 = 'aba', 'abccba', 'abccbd'
    print(is_string_palindrome(str1, 0, len(str1) - 1))
    print(is_string_palindrome(str2, 0, len(str2) - 1))
    print(is_string_palindrome(str3, 0, len(str3) - 1))
