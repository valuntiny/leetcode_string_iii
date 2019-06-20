'''
Quest:
    Implement a basic calculator to evaluate a simple expression string.
    The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
    The integer division should truncate toward zero.

    Example 1:
    Input: "3+2*2"
    Output: 7

    Example 2:
    Input: " 3/2 "
    Output: 1

    Example 3:
    Input: " 3+5 / 2 "
    Output: 5

    Note:
    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.

Solution:
    - use stack [] , num and sign ("+" in the beginning), for a formula like 1 + 2 * 3 + 4 / 5 - 6
        first: num = 1, "sign" = "+", []
        then: meet "+", so we stack ("sign"+num), sign = the new "+"
'''


class Solution:
    def calculate(self, s):
        if not s:
            return 0

        stk, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")

            # when reach a sign or the end of input, we do calculation
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "+":
                    stk.append(num)
                elif sign == "-":
                    stk.append(-num)
                elif sign == "*":
                    stk.append(num * stk.pop())
                else: # the truncated division
                    tmp = stk.pop()
                    if tmp / num < 0 and tmp % num != 0:
                        stk.append(tmp // num + 1)
                    else:
                        stk.append(tmp // num)
                sign = s[i]
                num = 0

        return sum(stk)

test = Solution()
x = " 3+5 / 2 "
print(test.calculate(x))
