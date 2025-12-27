from board import Board
from queue import Queue

class Search:
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