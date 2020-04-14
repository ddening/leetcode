from typing import List

class Solution:
    sol = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.sol.clear()                                    # just for leetcode
        result = self.nQueen(n, 0)
        return self.sol

    def nQueen(self, n: int, row: int, hasSolution: bool = False, queens=dict()):
        if row == n:
            return self.fillMap(n, queens)

        result = []

        for column in range(n):
            fieldIsSafe = True

            # check if current field is safe from all previous queens
            for qRow in queens:
                if queens[qRow] == column or row - column == qRow - queens[qRow] or row + column == qRow + queens[qRow]:
                    fieldIsSafe = False
                    break

            if fieldIsSafe:
                queens[row] = column
                result = self.nQueen(n, row + 1, hasSolution, queens.copy())
                if len(result) != 0 and result not in self.sol:
                    self.sol.append(result)
        return result

    def fillMap(self, n: int, hashMap: dict) -> List:
        s = []
        e = []
        for i in range(n):
            s.append(["."] * n)
        for x in hashMap:
            s[x][hashMap[x]] = "Q"
        for x in s:
            e += self.listToString(x)
        return e

    def listToString(self, s):
        return ["".join(s)]

solution = Solution()
foo = solution.solveNQueens(1)
print(foo)
foo = solution.solveNQueens(2)
print(foo)
foo = solution.solveNQueens(3)
print(foo)
foo = solution.solveNQueens(4)
print(foo)
foo = solution.solveNQueens(5)
print(foo)