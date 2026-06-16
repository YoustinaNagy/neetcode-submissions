class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =0
        assigned = True
        for r in range(len(matrix)) :
            if target < matrix[r][0]:
                row = r-1
                assigned = False 
                break
            elif target == matrix[r][0]:
                return True 
        
        if row ==-1: row+=1
        if assigned : row = len(matrix)-1
        for c in range(len(matrix[row])) :
            if target == matrix[row][c]:
                return True 
        return False 


        