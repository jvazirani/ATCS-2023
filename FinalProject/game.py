class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        pass 

    def check_win(self):
        pass 

    def check_fail(self): 
        # should probably take in food item and time cooking for 
        pass 

    def play_game(self):
        while self.check_fail != True:
            #draw screen
            if self.check_win():
                print(" wins!")
                #draw win screen
                break
            