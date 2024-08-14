import tkinter as tk
from tkinter import messagebox

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Ajedrez")
        
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.selected_piece = None
        self.create_board()
        self.place_pieces()

    def create_board(self):
        self.board = []
        self.cells = {}
        colors = ["white", "gray"]
        for row in range(8):
            board_row = []
            for col in range(8):
                cell_color = colors[(row + col) % 2]
                cell = tk.Label(self.board_frame, bg=cell_color, width=8, height=4, borderwidth=1, relief="solid")
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", lambda event, r=row, c=col: self.cell_clicked(r, c))
                board_row.append(cell)
                self.cells[(row, col)] = None  # No piece initially
            self.board.append(board_row)

    def place_pieces(self):
        # Place pawns
        for col in range(8):
            self.cells[(1, col)] = "bp"  # Black pawn
            self.cells[(6, col)] = "wp"  # White pawn
        # Place other pieces
        piece_order = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for col, piece in enumerate(piece_order):
            self.cells[(0, col)] = "b" + piece  # Black pieces
            self.cells[(7, col)] = "w" + piece  # White pieces
        self.update_board()

    def cell_clicked(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        else:
            self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.cells[(row, col)]
        if piece:
            self.selected_piece = (row, col)
            self.highlight_cell(row, col, "yellow")

    def move_piece(self, row, col):
        old_row, old_col = self.selected_piece
        piece = self.cells[(old_row, old_col)]
        self.cells[(old_row, old_col)] = None
        self.cells[(row, col)] = piece
        self.update_board()
        self.selected_piece = None
        self.update_board()

    def highlight_cell(self, row, col, color):
        self.board[row][col].config(bg=color)

    def update_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                cell_color = colors[(row + col) % 2]
                self.board[row][col].config(bg=cell_color)
                piece = self.cells[(row, col)]
                if piece:
                    self.board[row][col].config(text=piece)
                else:
                    self.board[row][col].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
