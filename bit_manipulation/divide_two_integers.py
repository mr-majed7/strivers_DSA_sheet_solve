# https://leetcode.com/problems/divide-two-integers/description/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = True

        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = False

        n = abs(dividend)
        d = abs(divisor)
        res = 0

        while n >= d:
            count = 0

            while n >= (d << count + 1):
                count += 1
            res += 1 << count
            n -= d * (1 << count)
        if res >= 2147483648 and sign == True:
            res -= 1
        return res if sign else -res
