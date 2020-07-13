class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        strNumber = str(x)
        revNumber = int(strNumber[::-1])
        if x - revNumber == 0:
            return True
        else:
            return False

