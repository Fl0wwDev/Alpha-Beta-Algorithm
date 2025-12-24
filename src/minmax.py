from board import Board
from queue import Queue
import random as rnd

class MinMax:

    def __init__(self, board: Board, turn: int, ai_level: int, queue: Queue, max_player: bool):
        self._board = board
        self._turn = turn
        self._ai_level = ai_level
        self._queue = queue
        self._max_player = max_player

    @property
    def board(self) -> Board:
        return self._board
    
    @board.setter
    def board(self, board: Board):
        self._board = board 

    @property
    def turn(self) -> int:
        return self._turn
    
    @turn.setter
    def turn(self, turn: int):
        self._turn = turn

    @property
    def ai_level(self) -> int:
        return self._ai_level
    
    @ai_level.setter
    def ai_level(self, ai_level: int):
        self._ai_level = ai_level
    
    @property
    def queue(self) -> Queue:
        return self._queue
    
    @queue.setter
    def queue(self, queue: Queue):
        self._queue = queue

    @property
    def max_player(self) -> bool:
        return self._max_player
    
    @max_player.setter
    def max_player(self, max_player: bool):
        self._max_player = max_player
    
    def max_value(self, board: Board, turn: int, depth: int, max_depth: int):
        if board.check_victory():
            return -1
        if turn > 42:
            return 0
        if depth >= max_depth:
            return 0
        possible_moves = board.get_possible_moves()
        best_value = -2
        for move in possible_moves:
            updated_board = board.copy()
            updated_board.add_disk(move, turn % 2 + 1, update_display=False)
            value = self.min_value(updated_board, turn + 1, depth + 1, max_depth)
            if value > best_value:
                best_value = value
        return best_value

    def min_value(self, board: Board, turn: int, depth: int, max_depth: int):
        if board.check_victory():
            return 1
        if turn > 42:
            return 0
        if depth >= max_depth:
            return 0
        possible_moves = board.get_possible_moves()
        worst_value = 2
        for move in possible_moves:
            updated_board = board.copy()
            updated_board.add_disk(move, turn % 2 + 1, update_display=False)
            value = self.max_value(updated_board, turn + 1, depth + 1, max_depth)
            if value < worst_value:
                worst_value = value
        return worst_value


    def minimax_decision(self, board: Board, turn: int, ai_level: int, queue: Queue, max_player: bool):
        max_depth = 4 
        possible_moves = board.get_possible_moves()
        best_move = possible_moves[0]
        best_value = -2
        for move in possible_moves:
            updated_board = board.copy()
            updated_board.add_disk(move, turn % 2 + 1, update_display=False)
            value = self.min_value(updated_board, turn + 1, 1, max_depth)
            if value > best_value:
                best_value = value
                best_move = move
        queue.put(best_move)

    
    def alpha_beta_decision(board, turn, ai_level, queue, max_player):
        # random move (to modify)
        queue.put(board.get_possible_moves()[rnd.randint(0, len(board.get_possible_moves()) - 1)])


    def max_value_ab(self, board: Board, turn: int, alpha: int, beta: int):
        if board.check_victory():
            return -1
        if turn > 42:
            return 0
        possible_moves = board.get_possible_moves()
        value = -2
        for move in possible_moves:
            updated_board = board.copy()
            updated_board.add_disk(move, turn % 2 + 1, update_display=False)
            value = max(value, self.min_value_ab(updated_board, turn + 1, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value


    def min_value_ab(self, board: Board, turn: int, alpha: int, beta: int):
        if board.check_victory():
            return 1
        if turn > 42:
            return 0
        possible_moves = board.get_possible_moves()
        value = 2
        for move in possible_moves:
            updated_board = board.copy()
            updated_board.add_disk(move, turn % 2 + 1, update_display=False)
            value = min(value, self.max_value_ab(updated_board, turn + 1, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

