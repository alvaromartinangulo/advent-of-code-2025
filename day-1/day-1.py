import os

class Solver:
    def __init__(self, input_file):
        #Password is number of times we point to zero
        self.password = 0
        #We start the pointer at 50
        self.current_value = 50
        self.input_file = input_file
        
    def process_move(self, input_move: str):
        temp = self.current_value
        turns = int(input_move[1:])
        if input_move[0] == "R":
            temp += turns
            crosses, temp = divmod(temp, 100)
            self.password += crosses
        else:
            temp = (self.current_value - turns) % 100
            
            if self.current_value == 0:
                self.password += turns // 100
            elif turns > self.current_value:
                self.password += ((turns - self.current_value - 1) // 100) + 1
                if temp == 0:
                    self.password += 1
            elif turns == self.current_value:
                self.password += 1
            
        self.current_value = temp
                
                    
    def process_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, self.input_file)
        with open(file_path) as f:
            for input_move in f:
                self.process_move(input_move)
        return self.password
    
if __name__ == '__main__':
    solver = Solver("problem-input.txt")
    print("password: ", solver.process_file()) 