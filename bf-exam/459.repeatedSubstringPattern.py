#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1 = s + s
        if s in s1[1:-1]:
            return True
        return False


s = "babbabbabbabbab"
sol = Solution()
res = sol.repeatedSubstringPattern(s)
print(res)