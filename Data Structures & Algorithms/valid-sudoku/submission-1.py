class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box={}
        for row in range(3,10,3):
            for column in range(3,10,3):
                for i in range(row-3,row):
                    for j in range(column-3,column):
                        if board[i][j]==".":
                            continue  
                        else:  
                            box[board[i][j]]=box.get(board[i][j],0)+1

                            if box[board[i][j]]>1:
                                return False
                box={}

        rows={}
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue  
                else:  
                    rows[board[i][j]]=rows.get(board[i][j],0)+1

                    if rows[board[i][j]]>1:
                        return False
            rows={}

        columns={}
        for i in range(9):
            for j in range(9):
                if board[j][i]==".":
                    continue  
                else:  
                    columns[board[j][i]]=columns.get(board[j][i],0)+1

                    if columns[board[j][i]]>1:
                        return False
            columns={}

        return True
