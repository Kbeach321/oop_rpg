# you down with OOP, yeah you know meee #

############IMPORTS#################
import random

###########Classes##############
class Player:
    def __init__(self, name):
        self.name = name
        self.gear = []
        self.timespent = 0
        self.gold = 0
        self.level = 0


    def spendtime(self):
        self.timespent = self.timespent + random.choice(range(5))

    def farmgold(self):
        if self.timespent <= 5:
            self.gold = self.gold + 10
            self.level = self.level + 1
        elif self.timespent <= 10:
            self.gold = self.gold + 25
            self.level = self.level + 3
        elif self.timespent <= 20:
            self.gold = self.gold + 80
            self.level = self.level + 10
        elif self.timespent <= 24:
            self.gold = self.gold + 100
            self.level = self.level + 20
        return self.gold, self.level

    def op_gear(self):
        if self.gold <= 10:
            self.gear = "Rustic Shortsword"
        elif self.gold > 25 and self.gold < 80:
            self.gear = "Keen Longsword"
        elif self.gold > 80 and self.gold <190:
            self.gear = "Flaming Morning"
        elif self.gold >= 200:
            self.gear = "One Punch Man Gauntlet"

    def gains(self):
        if self.timespent <= 5:
            print (f"{self.name} grinded for {self.timespent} Hours and recieved {self.gold} Gold")
            print (f"{self.name} has achieved {self.level} levels and a {self.gear}!")
        elif self.timespent <= 10:
            print (f"{self.name} grinded for {self.timespent} Hours and recieved {self.gold} Gold")
            print (f"{self.name} has achieved {self.level} Levels and a {self.gear}!")
        elif self.timespent <= 20:
            print (f"{self.name} grinded for {self.timespent} Hours and recieved {self.gold} Gold")
            print (f"{self.name} has achieved {self.level} Levels and a {self.gear}!")
        elif self.timespent <= 24:
            print (f"{self.name} grinded for {self.timespent} Hours and recieved {self.gold} Gold")
            print (f"{self.name} has achieved {self.level} Levels and a {self.gear}!")


################## variable = class(DEFINITION) ####################
noob = Player("The Noob King")
############################## BODY ###########################
while noob.gold <= 200:
    noob.spendtime()
    noob.farmgold()
    noob.op_gear()
    noob.gains()
    input()
