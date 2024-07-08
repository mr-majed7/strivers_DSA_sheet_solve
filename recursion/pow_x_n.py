# https://leetcode.com/problems/powx-n/description/

cclass Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            result = helper(x * x, n//2)

            return result * x if n%2 !=0 else result

        result = helper(x,abs(n))
        return result if n >= 0 else 1/resultlass Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x == 0:
                return 0

            if n == 0:
                return 1

            result = helper(x * x, n//2)

            return result * x if n%2 !=0 else result

        result = helper(x,abs(n))
        return result if n >= 0 else 1/result
