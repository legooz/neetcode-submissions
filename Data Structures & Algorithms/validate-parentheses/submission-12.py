class Solution:
    def isValid(self, s: str) -> bool:
        
        arr = []

        if not s:
            return False

        for ch in s:

            if ch == "(" or ch == "{" or ch == "[":
                arr.append(ch)
                print("append:", arr)
            
            elif ch == ")":
                if not arr:
                    return False
                if arr: 
                    if arr[-1] == "(":
                        arr.pop()
                        print("", arr)
                    else:
                        return False
            
            elif ch == "]":
                if not arr:
                    return False

                if arr:
                    if arr[-1] == "[":
                        arr.pop()
                        print("", arr)
                    else:
                        return False

            elif ch == "}":
                if not arr:
                    return False
                if arr:
                    if arr[-1] == "{":
                        arr.pop()
                        print(arr)
                    else:
                        return False

            else:
                return False
                

        
        if not arr:
            return True

        return False