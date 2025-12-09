import os

class Solver: 
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.validRanges = []
        self.totalValue = 0
                          
    def process_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, self.input_file)
        total_valid = 0
        with open(file_path) as f:
            seenEmpty = False
            for line in f:
                line = line.strip()
                if not line:
                    seenEmpty = True
                    self.compact_ranges()
                    continue
                if not seenEmpty:
                    self.process_range(line)
                    
            for validRange in self.validRanges:
                total_valid += validRange[1] - validRange[0] + 1
                        
        return total_valid
        
                           
    def process_range(self, range: str) -> None:
        vals = [int(x) for x in range.split("-")]
        self.validRanges.append(vals)
        
    def compact_ranges(self):
        compactRanges = []
        #Sort based on the first value
        self.validRanges.sort(key=lambda x: x[0])
        for validRange in self.validRanges:
            if not compactRanges or compactRanges[-1][1] < validRange[0]:
                compactRanges.append(validRange)
            elif compactRanges[-1][1] < validRange[1]:
                compactRanges[-1][1] = validRange[1]
        self.validRanges = compactRanges
        
        
    def process_value(self, value: str) -> bool:
        value = int(value)
        for range in self.validRanges:
            if range[0] <= value and range[1] >= value:
                return True
            if range[0] > value:
                return False
        return False
    
if __name__ == '__main__':
    solver = Solver("problem-input.txt")
    print("password: ", solver.process_file())