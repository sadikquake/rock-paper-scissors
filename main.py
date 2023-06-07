import random, time
from tkinter import *

class Game:
    def __init__(self):
        # 0 - rock, 1 - paper, 2 - scissors
        self.variants = [0, 1, 2]
        self.y_wins = 0
        self.c_wins = 0

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
                    print('You have won!')
                else:
                    self.c_wins += 1
                    print('You have lost!')
            else:
                print('You have chosen a non-existent option')
        except:
            print('You have chosen the wrong option')

    # Creating the graphical interface
    def get_game_interface(self):
        # params of window
        win = Tk()
        win.geometry('600x400')
        win.title('Rock - paper - scissors')
        win.iconbitmap('./i/icon.ico')
        win.resizable(width=False, height=False)
        win.configure(bg='#fcf2f0')

        # score of user
        y_score = Label(win, text='0', font=('Arial', 15), justify='left')
        y_score.place(x=120, y=35)

        # score of computer
        c_score = Label(win, text='0', font=('Arial', 15), justify='right')
        c_score.place(x=440, y=35)

        # creating buttons
        b_i_r = PhotoImage(file='./i/btn/0.png')
        b_i_r_btn = Button(win, image=b_i_r, command=lambda: self.play(0), bd=0)
        b_i_r_btn.place(x=120, y=330)

        b_i_p = PhotoImage(file='./i/btn/1.png')
        b_i_p_btn = Button(win, image=b_i_p, command=lambda: self.play(1), bd=0)
        b_i_p_btn.place(x=280, y=330)

        b_i_s = PhotoImage(file='./i/btn/2.png')
        b_i_s_btn = Button(win, image=b_i_s, command=lambda: self.play(2), bd=0)
        b_i_s_btn.place(x=440, y=330)

        win.mainloop()

gameClass = Game()
gameClass.get_game_interface()