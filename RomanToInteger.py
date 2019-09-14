# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_list = []
        index = 0
        while index < len(s):
            cur = s[index]
            if cur == 'I':  # or cur == 'X' or cur == 'C' :
                if index + 1 != len(s):
                    if s[index+1] == 'V':
                        result_list.append(4)
                        index+=2
                    elif s[index+1] == 'X':
                        result_list.append(9)
                        index += 2
                    else:
                        result_list.append(1)
                        index += 1
                else:
                    result_list.append(1)
                    index +=1
            elif cur == 'X':  # or cur == 'X' or cur == 'C' :
                if index + 1 != len(s):
                    if s[index + 1] == 'L':
                        result_list.append(40)
                        index += 2
                    elif s[index + 1] == 'C':
                        result_list.append(90)
                        index += 2
                    else:
                        result_list.append(10)
                        index += 1
                else:
                    result_list.append(10)
                    index +=1
            elif cur == 'C':  # or cur == 'X' or cur == 'C' :
                if index + 1 != len(s):
                    if s[index + 1] == 'D':
                        result_list.append(400)
                        index += 2
                    elif s[index + 1] == 'M':
                        result_list.append(900)
                        index += 2
                    else:
                        result_list.append(100)
                        index += 1
                else:
                    result_list.append(100)
                    index+=1
            elif cur == 'V':
                result_list.append(5)
                index +=1
            elif cur == 'L':
                result_list.append(50)
                index += 1
            elif cur == 'D':
                result_list.append(500)
                index += 1
            else:
                result_list.append(1000)
                index += 1
        return []

s = Solution()
print(s.romanToInt('MCMXCIV'))