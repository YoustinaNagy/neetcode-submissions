class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mapr={}
        mapc={}
        map3={}
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num =="." : continue 
                r = mapr.get(row,set())
                c= mapc.get(col ,set())

                cub = map3.get((row//3,col//3) , set())
                if num in r or  num in c or num in cub :
                    return False 
                r.add(num)
                c.add(num)
                cub.add (num)
                mapr[row] = r
                mapc[col]= c
                map3[(row//3,col//3)] = cub
        return True 
        
        