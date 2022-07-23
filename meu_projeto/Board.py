from colorama import Fore, Back, Style

class Board:
    def __init__(self) -> None:
        self.matrix = [
            ['X', ' ', 'O'],
            [' ', 'X', 'O'],
            [' ', ' ', 'O']
        ]

    def __str__(self) -> str:

        for index_line, line in enumerate(self.matrix):
            for index_col, col in enumerate(line):
                color = Fore.CYAN
                if (col == "X"):
                    color = Fore.RED
                el = color + col + Style.RESET_ALL
                self.matrix[index_line][index_col] = el
        

        return """
       col 1   col 2   col 3
             |       |       
line 1   {}   |   {}   |   {}   
      _______|_______|_______
             |       |      
line 2   {}   |   {}   |   {}    
      _______|_______|_______  
             |       |      
line 3   {}   |   {}   |   {}    
             |       |     
        """.format(
            self.matrix[0][0],
            self.matrix[0][1],
            self.matrix[0][2],
            self.matrix[1][0],
            self.matrix[1][1],
            self.matrix[1][2],
            self.matrix[2][0],
            self.matrix[2][1],
            self.matrix[2][2])