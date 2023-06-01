import random

class Game:
    def __init__(self):
        # 0 - rock, 1 - paper, 2 - scissors
        self.variants = [0, 1, 2]
        self.y_wins = 0
        self.c_wins = 0

    def play(self):
        c_choice = random.choice(self.variants)
        y_choice = input('Choose your option: ')

        # checking your selected option
        try:
            y_choice = int(y_choice)

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

gameClass = Game()
gameClass.play()