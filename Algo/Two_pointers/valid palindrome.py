import re
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        check = True
        for i in range(len(s)):
            reverse_i = len(s)-i-1
            if s[i] != s[reverse_i]:
                check = False
                break
        return check, s

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
