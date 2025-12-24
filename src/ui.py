import tkinter as tk
from tkinter import ttk

class UI:
    def __init__(self):
        self.disk_color = ['white', 'red', 'orange']
        self.disks = list()
        self.player_type = ['human']
        
        self.width = 700
        self.row_width = self.width // 7
        self.row_height = self.row_width
        self.height = self.row_width * 6
        self.row_margin = self.row_height // 10
        
        self.window = None
        self.canvas = None
        self.information = None
        self.combobox_player1 = None
        self.combobox_player2 = None
        self.button_new_game = None
        self.button_quit = None
        self.game = None

    def initialize_player_types(self):
        self.player_type.append('AI: minimax')
        for i in range(42):
            self.player_type.append('AI: alpha-beta level '+str(i+1))

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Connect 4")
    
    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, bg="blue", width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, columnspan=2)
    
    def draw_grid(self):
        for i in range(7):
            self.disks.append(list())
            for j in range(5, -1, -1):
                disk = self.canvas.create_oval(
                    self.row_margin + i * self.row_width, 
                    self.row_margin + j * self.row_height, 
                    (i + 1) * self.row_width - self.row_margin,
                    (j + 1) * self.row_height - self.row_margin, 
                    fill='white'
                )
                self.disks[i].append(disk)
    
    def create_information_label(self):
        self.information = tk.Label(self.window, text="")
        self.information.grid(row=1, column=0, columnspan=2)
    
    def create_player_selectors(self):
        label_player1 = tk.Label(self.window, text="Player 1: ")
        label_player1.grid(row=2, column=0)
        self.combobox_player1 = ttk.Combobox(self.window, state='readonly')
        self.combobox_player1.grid(row=2, column=1)
        self.combobox_player1['values'] = self.player_type
        self.combobox_player1.current(0)
        
        label_player2 = tk.Label(self.window, text="Player 2: ")
        label_player2.grid(row=3, column=0)
        self.combobox_player2 = ttk.Combobox(self.window, state='readonly')
        self.combobox_player2.grid(row=3, column=1)
        self.combobox_player2['values'] = self.player_type
        self.combobox_player2.current(6)
    
    def create_buttons(self):
        self.button_new_game = tk.Button(self.window, text='New game', command=self.game.launch)
        self.button_new_game.grid(row=4, column=0)
        
        self.button_quit = tk.Button(self.window, text='Quit', command=self.window.destroy)
        self.button_quit.grid(row=4, column=1)
    
    def bind_mouse_events(self):
        self.canvas.bind('<Button-1>', self.game.click)
    
    def launch_ui(self, game: object):
        self.game = game
        
        self.create_window()
        self.create_canvas()
        self.draw_grid()
        self.create_information_label()
        self.create_player_selectors()
        self.create_buttons()
        self.bind_mouse_events()
        
        self.window.mainloop()