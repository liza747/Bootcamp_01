from collections import Counter

class Game:
    def __init__ (self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for loop in range(self.matches):
            if player1.step == 1 and player2.step == 1:
                pass
            if player1.step == 2 and player2.step == 2:
                player1.purse += 2
                player2.purse += 2
            if player1.step == 1 and player2.step == 2:
                player1.purse += 3
                player2.purse -= 1
            if player1.step == 2 and player2.step == 1:
                player1.purse -= 1
                player2.purse += 3
            player1.alg_steps(player2.step)
            player2.alg_steps(player1.step)
        self.registry.update({player1.type: player1.purse, player2.type: player2.purse})

    def top3(self):
        for top in self.registry.most_common(3):
            print (top)

    def default(self):
        self.play(Copycat(), Cheater()) 
        self.play(Copycat(), Cooperator()) 
        self.play(Copycat(), Grudger()) 
        self.play(Copycat(), Detective()) 
        self.play(Cheater(), Cooperator()) 
        self.play(Cheater(), Grudger()) 
        self.play(Cheater(), Detective()) 
        self.play(Cooperator(), Grudger()) 
        self.play(Cooperator(), Detective()) 
        self.play(Grudger(), Detective()) 
        self.top3()

class Player:
    def __init__ (self):
        self.step = 0
        self.purse = 0
        self.type = ""

    def alg_steps(self, p_step):
        pass

class Cheater(Player):
    def __init__(self):
        super().__init__()
        self.step = 1
        self.type = "Cheater"

class Cooperator(Player):
    def __init__(self):
        super().__init__()
        self.step = 2
        self.type = "Cooperator"

class Copycat(Player):
    def __init__(self):
        super().__init__()
        self.step = 2
        self.type = "Copycat"

    def alg_steps(self, p_step):
        self.step = p_step

class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.step = 2
        self.type = "Grudger"
        
    def alg_steps(self, p_step):
        if p_step == 1:
            self.step = 1

class Detective(Player):
    def __init__(self):
        super().__init__()
        self.step = 2
        self.d_step = False
        self.type = "Detective"
        self.loop = 1

    def alg_steps(self, p_step):
        if self.loop < 4:
            if self.loop == 1:
                self.step = 1
            if p_step == 1:
                self.d_step = True
            if self.loop == 2:
                self.step = 2
            if self.loop == 3:
                self.step = 2
        else:
            if self.d_step == True:
                self.step = p_step
            else:
                self.step = 1
        self.loop+=1

if __name__ == "__main__":
    game = Game()
    game.default()