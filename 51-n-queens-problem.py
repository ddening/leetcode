from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = self.nQueen(n, 0)[1]
        print(result)

    def nQueen(self, n: int, row: int, hasSolution: bool = False, queens = dict()):
        if row == n:
            return True, self.fillMap(n, queens)

        for column in range(n):
            fieldIsSafe = True

            # check if current field is safe from all previous queens
            for qRow in queens:
                if queens[qRow] == column or row - column == qRow - queens[qRow] or row + column == qRow + queens[qRow]:
                    fieldIsSafe = False
                    break

            if fieldIsSafe:
                queens[row] = column
                hasSolution, result = self.nQueen(n, row + 1, hasSolution, queens.copy())   # copy.deepcopy(queens)
                if hasSolution is True:
                    return hasSolution, result
        return False, [None]

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
solution.solveNQueens(4)