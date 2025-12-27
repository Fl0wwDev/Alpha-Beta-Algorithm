from threading import Thread
from queue import Queue
from minmax import MinMax
from alpha_beta import AlphaBeta
from ui import UI
from board import Board

class Connect4:

    def __init__(self, ui: UI, board: Board):
        self.human_turn = False
        self.turn = 1
        self.players = (0, 0)
        self.ai_move = Queue()
        self.ui = ui
        self.board = board

    def current_player(self):
        return 2 - (self.turn % 2)

    def launch(self):
        self.board.reinit()
        self.turn = 0
        self.ui.information['fg'] = 'black'
        self.ui.information['text'] = "Turn " + str(self.turn) + " - Player " + str(
            self.current_player()) + " is playing"
        self.human_turn = False
        self.players = (self.ui.combobox_player1.current(), self.ui.combobox_player2.current())
        self.handle_turn()

    def move(self, column: int):
        if not self.board.column_filled(column):
            self.board.add_disk(column, self.current_player())
            self.handle_turn()

    def click(self, event: object):
        if self.human_turn:
            column = event.x // self.ui.row_width
            self.move(column)

    def ai_turn(self, ai_level: int):
        if ai_level == 1:
            minmax = MinMax(self.board, self.turn, ai_level, self.ai_move, True)
            # Minimax (index 1 in combobox)
            Thread(target=minmax.minimax_decision, args=(self.board, self.turn, ai_level, self.ai_move, self.current_player(),)).start()
        else:
            alpha_beta = AlphaBeta(self.board, self.turn, ai_level, self.ai_move, True)
            # Alpha-beta (index 2+ in combobox)
            Thread(target=alpha_beta.alpha_beta_decision, args=(self.board, self.turn, ai_level - 1, self.ai_move, self.current_player(),)).start()
        self.ai_wait_for_move()

    def ai_wait_for_move(self):
        if not self.ai_move.empty():
            self.move(self.ai_move.get())
        else:
            self.ui.window.after(100, self.ai_wait_for_move)

    def handle_turn(self):
        self.human_turn = False
        if self.board.check_victory():
            self.ui.information['fg'] = 'red'
            self.ui.information['text'] = "Player " + str(self.current_player()) + " wins !"
            return
        elif self.turn >= 42:
            self.ui.information['fg'] = 'red'
            self.ui.information['text'] = "This a draw !"
            return
        self.turn = self.turn + 1
        self.ui.information['text'] = "Turn " + str(self.turn) + " - Player " + str(
            self.current_player()) + " is playing"
        if self.players[self.current_player() - 1] != 0:
            self.human_turn = False
            self.ai_turn(self.players[self.current_player() - 1])
        else:
            self.human_turn = True