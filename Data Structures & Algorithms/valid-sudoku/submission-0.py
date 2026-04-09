class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowStore= collections.defaultdict(set)
        columnStore= collections.defaultdict(set)
        threeStore= collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if  board[i][j] in rowStore[i] or board[i][j] in columnStore[j] or board[i][j] in threeStore[(i//3, j//3)]:
                    return False
                rowStore[i].add(board[i][j])
                columnStore[j].add(board[i][j])
                threeStore[(i//3, j//3)].add(board[i][j])
        return True
                