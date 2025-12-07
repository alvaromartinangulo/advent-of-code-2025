import os

class Solver: 
    def __init__(self, input_file: str):
        self.input_file = input_file
                          
    def process_file(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, self.input_file)
        with open(file_path) as f:
            lines = [list(line.strip()) for line in f]
        totalAccessible = 0
        removed = True
        while removed:
            removed = False
            for y in range(len(lines)):
                for x in range(len(lines[y])):
                    if self.process_coord(y, x, lines, 4):
                        lines[y][x] = "."
                        removed = True
                        totalAccessible += 1
                    
        return totalAccessible

    def process_coord(self, y_input: int, x_input: int, board: list[str], maxOccurences: int) -> bool:
        if board[y_input][x_input] != "@":
            return False
        occurences = 0
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for (y_add, x_add) in moves:
            #Skip values of the board that are invalid
            y, x = y_input + y_add, x_input + x_add
            if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]):
                continue
            if board[y][x] == "@":
                occurences += 1
        return occurences < maxOccurences
    
if __name__ == '__main__':
    solver = Solver("problem-input.txt")
    print("password: ", solver.process_file())