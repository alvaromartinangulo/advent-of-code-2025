import os

class Solver: 
    def __init__(self, input_file: str):
        self.input_file = input_file
                          
    def process_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, self.input_file)
        with open(file_path) as f:
            inputLine = f.readline()
        ranges = inputLine.split(",")
        totalSumRanges = 0
        for range in ranges:
            totalSumRanges += self.process_range(range)
        return(totalSumRanges)
        
    #Returns the sum of the ranges of the invalid ranges      
    def process_range(self, rangeStr: str) -> int:
        sumRangeInvalid = 0
        rangeNums = rangeStr.split("-")
        for num in range(int(rangeNums[0]), int(rangeNums[1]) + 1):
            if self.containsRepeatedSequence(num):
                sumRangeInvalid += num
        return sumRangeInvalid
            
    def containsRepeatedSequence(self, num: int) -> bool:
        numStr = str(num)
        lenStr = len(numStr)
        if lenStr == 1:
            return False
        for lenSequence in range(1, (lenStr//2) + 1):
            if lenStr % lenSequence != 0:
                continue
            sequence = numStr[0:lenSequence]
            allMatch = True
            for startingIndex in range(0, lenStr, lenSequence):
                currSequence = numStr[startingIndex: startingIndex + lenSequence]
                if sequence != currSequence:
                    allMatch = False
                    continue
            if allMatch: 
                return True
        return False
    
            
    
if __name__ == '__main__':
    solver = Solver("problem-input.txt")
    print("password: ", solver.process_file())