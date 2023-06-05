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

        # score

        score_text = Label(win, text='Score:', font=('Arial', 15))
        score_text.place(x=0, y=5)

        # score of user
        y_score = Label(win, text=f"{self.y_wins}", font=('Arial', 15), justify='left')
        y_score.place(x=50, y=35)

        # score of computer
        c_score = Label(win, text='0', font=('Arial', 15), justify='right')
        c_score.place(x=500, y=35)

        # creating buttons
        btn_rock = Button(win, text='Rock', font=('Arial', 15), command=lambda x=0: self.play(x))
        btn_paper = Button(win, text = 'Paper', font=('Arial', 15), command=lambda x=1: self.play(x))
        btn_scissors = Button(win, text='Scissors', font=('Arial', 15), command=lambda x=1: self.play(x))

        btn_rock.place(x=10, y=100, width=80, height=30)
        btn_paper.place(x=200, y=100, width=80, height=30)
        btn_scissors.place(x=400, y=100, width=80, height=30)

        win.mainloop()

gameClass = Game()
gameClass.get_game_interface()