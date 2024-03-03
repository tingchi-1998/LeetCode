#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_integer = {'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000}
        s = s.replace('IV', 'IIII') \
             .replace('IX', 'VIIII') \
             .replace('XL', 'XXXX') \
             .replace('XC', 'LXXXX') \
             .replace('CD', 'CCCC') \
             .replace('CM', 'DCCCC')
        
        return sum(map(roman_to_integer.get, s))

# @lc code=end

