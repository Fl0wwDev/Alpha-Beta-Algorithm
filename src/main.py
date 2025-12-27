from ui import UI
from connect4 import Connect4
from board import Board

def main():
    ui = UI()
    ui.initialize_player_types()
    board = Board(ui)
    game = Connect4(ui, board)
    ui.launch_ui(game)

if __name__ == "__main__":
    main()