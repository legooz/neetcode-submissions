class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):

        L = 0
        R = len(matrix[0]) - 1
        
        L_row = 0
        R_row = len(matrix) - 1

       
        while L_row <= R_row: 
            M = (L_row + R_row) // 2 # 1

            if(matrix[M][L] <= target <= matrix[M][R]):
                while L <= R:
                    mid = (L + R) // 2
                    if(matrix[M][mid] < target):
                        L = mid + 1
                    elif(matrix[M][mid] > target):
                        R = mid - 1
                    else:
                        return True
                return False
            elif(matrix[M][L] < target): # if 10 < 3
                L_row = M + 1
            elif(matrix[M][R] > target): # 20 > 3
                R_row = M - 1


        return False