class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        for i in range(len(arr)):
            if(len(arr) - 1 == i):
                arr[i] = -1
                break

            arrMax = arr[i+1]
            for j in range(i+1, len(arr)):    
                if(arr[j] > arrMax): 
                    arrMax = arr[j] #5

            arr[i] = arrMax


            
            print(arr, arrMax)
            
        return arr