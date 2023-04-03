import sys
sys.setExecutionLimit(600000) # let this take up to 10 minutes

import json
import time
import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self, prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
class WOFHumanPlayer(WOFPlayer):    # inherits WOFPlayer
    def getMove(self, category, obscuredPhrase, guessed):
        move = input("{} has ${}\n\nCategory: {}\nPhrase: {}\nGuessed: {}\n\nGuess a letter, phrasem or type 'exit' or 'pass':".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed))
        return move

class WOFComputerPlayer(WOFPlayer):     # inherits WOFPlayer
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)          # __init__ from parent with super()
        self.difficulty = difficulty    # new instance variable

    def smartCoinFlip(self):            # good or bad move. freq based on difficulty
        res = random.randint(1,10)
        if res <= self.difficulty:
            return True
        else:
            return False
        
    def getPossibleLetters(self, guessed):
        if self.prizeMoney < VOWEL_COST:
            return [i for i in LETTERS if i not in VOWELS and i not in guessed]
        else:
            return [i for i in LETTERS if i not in guessed]
        
    def getMove(self, category, obscuredPhrase, guessed):
        possibleMoves = self.getPossibleLetters(guessed)
        if possibleMoves == []:
            return 'pass'
        if self.smartCoinFlip():
            for i in SORTED
        
        

                
                
                

    

