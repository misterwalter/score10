import random

class Character():
    name = "Basic"
    score = 0
    goal_score = 10
    loud = True

    def __init__(self, loud=True):
        self.loud = loud

    def __str__(self):
        return self.name

    def turn(self, opponent):
        if self.loud:
            print("{} > {}".format(self.score, self.score+1))
        self.score += 1

class VampCharacter(Character):
    name = "Vampire"
    plus = .5
    minus = .5

    def turn(self, opponent):
        if self.loud:
            print("{} > {} and {} > {}".format(
                self.score, self.score+.8,
                self.score, self.score-.2
            ))
        self.score += .8
        opponent.score -= .2

class TankCharacter(Character):
    name = "Tank" 
    goal_score = 20

    def turn(self, opponent):
        if self.loud:
            print("{} > {}".format(self.score, self.score+1))
        self.score += .5

class JackpotCharacter(Character):
    name = "Jackpot"

    def turn(self, opponent):
        if self.loud:
            print("{} > {}".format(self.score, self.score+1))
        if random.randint(1,10) is 10:
            self.score += 10

class AggroCharacter(Character):
    name = "Aggro" 
    sleepy = random.choice((True, False))

    def turn(self, opponent):
        if self.loud:
            print("{} > {}".format(self.score, self.score+1))
        if not self.sleepy:
            self.score += 2
        self.sleepy = not self.sleepy

class HealerCharacter(Character):
    name = "Healer"

    def turn(self, opponent):
        opponent.score -= 1

class MageCharacter(Character):
    name =  "Mage"
    power = 0

    def turn(self, opponent):
        self.power += 1
        if self.power >= opponent.goal_score - self.score: #-score makes them smarter, +++winrate
            self.score += self.power
            self.power = 0

class GamblerCharacter(Character):
    name = "Gambler"
    odds = [-4, -2, 0, 2, 4, 6] #+6 total advantage / 6 slots = 1/turn

    def turn(self, opponent):
        self.score += random.choice(self.odds)

class TaxCharacter(Character):
    name = "Tax"
    rate = .1

    def turn(self, opponent):
        self.score += self.rate * opponent.goal_score

#######################################################################################################################
#######################################################################################################################

class Game():
    goal_score = 10
    turn_max = 1000 #maximum number of turns to prevent infinite games - most won't got this long

    def __init__(self, p1, p2, loud=True):
        self.turn_curr = 0
        self.p1 = p1
        self.p2 = p2
        self.loud = loud

    def play(self):
        while self.p1.score < self.p2.goal_score and self.p2.score < self.p1.goal_score and self.turn_curr < self.turn_max:
            self.turn_curr += 1
            if self.loud:
                print("Turn {}:".format(self.turn_curr))
            self.p1.turn(self.p2)
            self.p2.turn(self.p1)

        if self.p1.score >= self.p2.goal_score and self.p2.score >= self.p1.goal_score:
            return 0
        elif self.p1.score >= self.p2.goal_score:
            return 1
            #print("{} defeats {}!\nScore of {} to {}.".format(self.p1, self.p2, self.p1.score, self.p2.score))
        elif self.p2.score >= self.p1.goal_score:
            return -1
            #print("{} defeats {}!\nScore of {} to {}.".format(self.p2, self.p1, self.p1.score, self.p2.score))
        else:
            return 0
            #print("Draw between {} and {} \nScore of {} to {}.".format(self.p1, self.p2, self.p1.score, self.p2.score))

characters = [Character, AggroCharacter,
    GamblerCharacter, HealerCharacter, JackpotCharacter, 
    TankCharacter, TaxCharacter, MageCharacter, VampCharacter]
print(("{:10}|"+ ("{:4}|"*len(characters)) ).format("", * [str(c())[:4] for c in characters]))
for player1 in characters:
    record = []
    for player2 in characters:
        wins = 0
        loud = False#player1 is not player2
        for i in range(10):
            wins += Game(player1(loud), player2(loud), loud).play()
        record.append(wins)
    print(("{:10}|"+ ("{:4}|"*len(characters)) ).format(player1(), * record))
