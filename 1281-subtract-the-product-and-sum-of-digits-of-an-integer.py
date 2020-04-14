class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product = 1
        s = 0

        for x in str(n):
            product *= int(x)
            s += int(x)

        return product - s
