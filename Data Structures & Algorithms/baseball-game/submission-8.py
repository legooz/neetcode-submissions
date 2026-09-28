class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = 0
        record = []
        
        for ops in operations:
            
            if ops.isdigit():
                score = int(ops)
                record.append(score)
                print("Is digit: ", record)
            elif ops.removeprefix("-").isdigit():
                score = int(ops)
                record.append(score)
            elif ops == "+":
                score = record[-1] + record[-2]
                record.append(score)
                print("+", record)

            elif ops == "C":
                record.pop()
                print("C", record)

            elif ops == "D":
                record.append(record[-1] * 2)
                print("D", record)
        


        return sum(record)

