class Solution:
    def getSum(self, a: int, b: int) -> int:
        a, b = a+1000, b+1000
        while b:
            a, b = a^b, (a&b) << 1
        return a-2000
