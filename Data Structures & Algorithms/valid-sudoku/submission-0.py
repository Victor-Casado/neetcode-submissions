class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #columns
        for column in range(0,9):
            seen = self.newSeen()
            for row in board:
                if (seen[row[column]]):
                    return False
                if (row[column] != "."):
                    seen[row[column]] = True
        #rows
        for row in board:
            seen = self.newSeen()
            for number in row:
                if (seen[number]):
                    return False
                if (number != "."):
                    seen[number] = True
        #grids
        startingNums = [0, 3, 6]
        for num in startingNums:
            for num2 in startingNums:
                seen = self.newSeen()
                numbersToCheck = [
                    board[num2][num],
                    board[num2+1][num],
                    board[num2+2][num],
                    board[num2][num+1],
                    board[num2+1][num+1],
                    board[num2+2][num+1],
                    board[num2][num+2],
                    board[num2+1][num+2],
                    board[num2+2][num+2]
                ]
                for checkThis in numbersToCheck:
                    if seen[checkThis]:
                        return False
                    if (checkThis != "."):
                        seen[checkThis] = True
            
        return True
                


    def newSeen(self):
        return {
            ".": False,
            "1": False,
            "2": False,
            "3": False,
            "4": False,
            "5": False,
            "6": False,
            "7": False,
            "8": False,
            "9": False
        }