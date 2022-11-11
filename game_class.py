from tkinter import *

Font_tuple = ("Helvetica", 50, "bold")
Reset_font_tuple = ("Helvetica", 10, "bold")

WINING_COMBINATIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                       [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

class Initialize(Tk):
    def __init__(self):
        super().__init__()
        self.count=0
        self.x = []
        self.o = []
        self.buttons = []
        self.config(background='lightblue')
        self.title('Tic Tac Toe')


        # Game info Frame
        self.info_frame = Frame(self, bg="lightblue")
        self.info_frame.pack(fill=X)
        self.info_frame.columnconfigure(0, weight=1)
        self.info_label = Label(self.info_frame, text='READY!!!', bg="lightblue", font=Font_tuple)
        self.info_label.grid(row=0, column=0)

        # Reset button Framе
        self.reset_frame = Frame(self, bg="lightblue")
        self.reset_frame.pack(fill=X)
        self.reset_frame.columnconfigure(0, weight=1)
        self.reset_button = Button(self.reset_frame, text="New Game", width=10, font=Reset_font_tuple, bd=5, pady=10)

        # Main frame
        self.main_frame = Frame()
        self.main_frame.pack(expand=True)

        self.button = [None] * 9
        for i in range(9):
            r, c = divmod(i, 3)
            self.button[i] = Button(self.main_frame, height=2, width=5, font=Font_tuple,
                                       command=lambda n=i: self.playing(n))
            self.buttons.append(self.button[i])
            self.button[i].grid(row=r, column=c, sticky='nesw')
            
        self.mainloop()
    
    def playing(self, n):
        self.count += 1
        
        # Check for play turn for X player
        if (self.count % 2) != 0:
            self.button[n].configure(text='X', command=DISABLED, fg='red')
            self.info_label.configure(text='PLAYER O MOVE')
            self.x.append(n)
             
             # Check for win player X
            for win in WINING_COMBINATIONS:
                if all(num in self.x for num in win):
                    self.info_label.configure(text='PLAYER X WINS', fg='red')
                    for game_over_x in self.buttons:
                        game_over_x.configure(command=DISABLED)
                    self.create_newgame_button()

                # Check for TIE
                elif self.count == 9:
                    self.button[n].configure(text='X', command=DISABLED, fg='red')
                    self.info_label.configure(text='TIE!', fg="green")
                    self.create_newgame_button()

        # Check for play turn for O player
        elif (self.count % 2) == 0:
            self.button[n].configure(text='O', command=DISABLED, fg="blue")
            self.info_label.configure(text='PLAYER X MOVE')
            self.o.append(n)

            # Check for win player O
            for win in WINING_COMBINATIONS:
                if all(num in self.o for num in win):
                    self.info_label.configure(text='PLAYER O WINS', fg="blue")
                    for game_over_o in self.buttons:
                        game_over_o.configure(command=DISABLED)
                    self.create_newgame_button()                
    
    def create_newgame_button(self):
        self.reset_button.grid(row=0, column=0)
        self.reset_button.configure(command=self.reset)
    
    def reset(self):
        self.destroy()
        self.__init__()
    
    