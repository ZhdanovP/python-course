#Exercise 9
#
#Implement chess figure:
#
#    You should implement base class with checkStep method. This method is abstract (pass operator)
#    You should implement Horse, Elefant, and King figure with different implement of checkStep method
#    You should get from user figure name and next step coordinates: e2, e4…
#    Your program should be print new figure`s coordinates or error, if step not possible
#    No need check other figures on deck or check figure`s color

# Chess Desk
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = ['1', '2', '3', '4', '5', '6', '7', '8']

class Piece:
    def __init__(self, init_pos):
        self._position = init_pos
    def type(self):
        pass
    def move(self, end_pos):
        pass
    
class King(Piece):
    def __init__(self, init_pos):
        super().__init__(init_pos)
    def type(self):
        return 'King'
    def move(self, end_pos):
        if len(end_pos) != 2:
            return False
        else:
            index_row_current = row.index(self._position[0])
            index_col_current = col.index(self._position[1])
            index_row_next = row.index(end_pos[0])
            index_col_next = col.index(end_pos[1])
            if (index_row_next != -1 and index_col_next != -1 and
                (abs(index_row_next - index_row_current) == 1 or
                 abs(index_col_next - index_col_current) == 1)):
                self._position = end_pos
                print(f"King is moved to {self._position}")
                return True
            else:
                return False
            
class Elefant(Piece):
    def __init__(self, init_pos):
        super().__init__(init_pos)
    def type(self):
        return 'Elefant'
    def move(self, end_pos):
        # Implement move logic here
        self._position = end_pos
        print(f"Elefant is moved to {self._position}")
        return True
    
class Horse(Piece):
    def __init__(self, init_pos):
        super().__init__(init_pos)
    def type(self):
        return 'Horse'
    def move(self, end_pos):
        # Implement move logic here
        self._position = end_pos
        print(f"Horse is moved to {self._position}")
        return True
    
class Board:
    def __init__(self, *pieces):
        self.__pieces = pieces
    def move_piece(self, piece_type, next_step):
        count = 0
        for p in self.__pieces:
            if p.type() == piece_type and p.move(next_step):
                count += 1
        return count
        
board = Board(King('d4'), King('g3'), Elefant('a1'), Elefant('b2'), Horse('h7'))
print("Moved {} pieces".format(board.move_piece('King', 'd3')))
print("Moved {} pieces".format(board.move_piece('Elefant', 'g6')))
print("Moved {} pieces".format(board.move_piece('Horse', 'a4')))
