import os

class Solver: 
    def __init__(self, input_file: str):
        self.input_file = input_file
                          
    def process_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, self.input_file)
        with open(file_path) as f:
            banks = f.readlines()
        totalJoltage = 0
        for bank in banks:
            totalJoltage += self.getJoltage(bank, 12)
        return(totalJoltage)
       
            
    def getJoltage(self, bank:str, digits:int) -> int:
        pointers = [_ for _ in range(digits)]
        maxVal = "".join([bank[i] for i in pointers])
        while pointers[-1] < len(bank):
            maxVal = max(int(maxVal), int("".join([bank[i] for i in pointers])))
            #loop over the indices of the pointers
            for i in range(len(pointers) - 1):
                #i is the parent pointer (more important value)
                if bank[pointers[i + 1]] > bank[pointers[i]]:
                    for j in range(i, len(pointers) - 1):
                        pointers[j] = pointers[j + 1]
                    break
            pointers[-1] += 1
            
        print(bank, maxVal)
        return int(maxVal)
    
if __name__ == '__main__':
    solver = Solver("problem-input.txt")
    print("password: ", solver.process_file())