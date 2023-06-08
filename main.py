import random, time
from tkinter import *

class Game:
    def __init__(self):
        # 0 - rock, 1 - paper, 2 - scissors
        self.variants = [0, 1, 2]
        self.y_wins = 0
        self.c_wins = 0

        # Creating the graphical interface
        self.main_color = '#fcf2f0'
        self.images = {
            'icon': './i/icon.ico',
            'btn_rock': './i/btn/0.png',
            'btn_paper': './i/btn/1.png',
            'btn_scissors': './i/btn/2.png'
        }

        # params of window
        self.win = Tk()
        self.win.geometry('600x400')
        self.win.title('Rock - paper - scissors')
        self.win.iconbitmap(self.images['icon'])
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=self.main_color)

        # score of user
        self.y_score = Label(self.win, text='0', font=('Arial', 15), justify='left', background=self.main_color)
        self.y_score.place(x=120, y=25)

        # score of computer
        self.c_score = Label(self.win, text='0', font=('Arial', 15), justify='right', background=self.main_color)
        self.c_score.place(x=440, y=25)

        # creating buttons
        self.b_i_r = PhotoImage(file=self.images['btn_rock'])
        self.b_i_r_btn = Button(self.win, image=self.b_i_r, command=lambda: self.play(0), bd=0)
        self.b_i_r_btn.place(x=120, y=330)

        self.b_i_p = PhotoImage(file=self.images['btn_paper'])
        self.b_i_p_btn = Button(self.win, image=self.b_i_p, command=lambda: self.play(1), bd=0)
        self.b_i_p_btn.place(x=280, y=330)

        self.b_i_s = PhotoImage(file=self.images['btn_scissors'])
        self.b_i_s_btn = Button(self.win, image=self.b_i_s, command=lambda: self.play(2), bd=0)
        self.b_i_s_btn.place(x=440, y=330)

    # play game
    def play(self, player_choise):

        c_choice = random.choice(self.variants)
        y_choice = player_choise

        # checking your selected option
        try:
            if isinstance(y_choice, int) and y_choice in self.variants:
                if c_choice == y_choice:
                    print('Drawn')
                elif c_choice == 0 and y_choice == 1 or c_choice == 1 and y_choice == 2 or c_choice == 2 and y_choice == 0:
                    self.y_wins += 1
                    self.y_score.config(text=self.y_wins)
                    print('You have won!')
                else:
                    self.c_wins += 1
                    self.c_score.config(text=self.c_wins)
                    print('You have lost!')
            else:
                print('You have chosen a non-existent option')
        except:
            print('You have chosen the wrong option')

    def run(self):
        self.win.mainloop()

game = Game()
game.run()