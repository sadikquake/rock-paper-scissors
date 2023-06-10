import random, time
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

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
            'btn_scissors': './i/btn/2.png',
            'ga_0': './i/game/0.gif',
            'ga_00': './i/game/00.gif',
            'ga_01': './i/game/01.gif',
            'ga_02': './i/game/02.gif',
            'ga_10': './i/game/10.gif',
            'ga_11': './i/game/11.gif',
            'ga_12': './i/game/12.gif',
            'ga_20': './i/game/20.gif',
            'ga_21': './i/game/21.gif',
            'ga_22': './i/game/22.gif'
        }

        # params of window
        self.win = Tk()
        self.win.geometry('600x510')
        self.win.title('Rock - paper - scissors')
        self.win.iconbitmap(self.images['icon'])
        self.win.resizable(width=False, height=False)
        self.win.configure(bg=self.main_color)

        # score of user
        self.y_score = Label(self.win, text='0', font=('Arial', 15), justify='left', background=self.main_color)
        self.y_score.place(x=120, y=10)

        # score of computer
        self.c_score = Label(self.win, text='0', font=('Arial', 15), justify='right', background=self.main_color)
        self.c_score.place(x=440, y=10)

        # creating buttons
        self.b_i_r = PhotoImage(file=self.images['btn_rock'])
        self.b_i_r_btn = Button(self.win, image=self.b_i_r, command=lambda: self.play(0), bd=0)
        self.b_i_r_btn.place(x=120, y=450)

        self.b_i_p = PhotoImage(file=self.images['btn_paper'])
        self.b_i_p_btn = Button(self.win, image=self.b_i_p, command=lambda: self.play(1), bd=0)
        self.b_i_p_btn.place(x=280, y=450)

        self.b_i_s = PhotoImage(file=self.images['btn_scissors'])
        self.b_i_s_btn = Button(self.win, image=self.b_i_s, command=lambda: self.play(2), bd=0)
        self.b_i_s_btn.place(x=440, y=450)

        # label for animation
        self.ga = PhotoImage(file=self.images['ga_0'])
        self.ga_lab = Label(self.win, image=self.ga)
        self.ga_lab.place(x=40, y=40)

        self.win.protocol('WM_DELETE_WINDOWS', self.exit)

    # play game
    def play(self, player_choise):
        self.get_image('00')

        c_choice = random.choice(self.variants)
        y_choice = player_choise

        # checking your selected option
        try:
            if isinstance(y_choice, int) and y_choice in self.variants:
                self.get_image('0')
                self.get_image(str(y_choice) + str(c_choice))
                if c_choice == y_choice:
                    messagebox.showinfo('showinfo', 'Drown')
                elif c_choice == 0 and y_choice == 1 or c_choice == 1 and y_choice == 2 or c_choice == 2 and y_choice == 0:
                    self.y_wins += 1
                    self.y_score.config(text=self.y_wins)
                    messagebox.showinfo('showinfo', 'You have won!')
                else:
                    self.c_wins += 1
                    self.c_score.config(text=self.c_wins)
                    messagebox.showinfo('showinfo', 'You have lost!')
            else:
                print('You have chosen a non-existent option')
        except:
            print('You have chosen the wrong option')

    # initializing the graphical interface
    def run(self):
        self.win.mainloop()

    # exit game (close window)
    def exit(self):
        self.win.destroy()

    # get image or play gif animation
    def get_image(self, file_key):
        try:
            with Image.open(self.images['ga_' + file_key]) as i:
                if getattr(i, 'is_animated', False):
                    for frame in ImageSequence.Iterator(i):
                        self.ga = ImageTk.PhotoImage(frame)
                        self.ga_lab.config(image=self.ga)
                else:
                    self.ga = PhotoImage(file=self.images['ga_' + file_key])
                    self.ga_lab.config(image=self.ga)
        except IOError:
            return False

game = Game()
game.run()