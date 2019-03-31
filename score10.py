import random
from collections import defaultdict


class Character():
    """Base class for all characters, with default functionality.

    Child classes don't need docstrings, because they should be very simple.
    """
    name = "Basic"
    score = 0
    goal_score = 10

    def __str__(self):
        return self.name

    def turn(self, opponent):
        self.score += 1


class VampCharacter(Character):
    name = "Vampire"

    def turn(self, opponent):
        self.score += .8
        opponent.score -= .2


class TankCharacter(Character):
    name = "Tank"
    goal_score = 20

    def turn(self, opponent):
        self.score += .5


class JackpotCharacter(Character):
    name = "Jackpot"

    def turn(self, opponent):
        if random.randint(1, 10) is 10:
            self.score += 10


class AggroCharacter(Character):
    name = "Aggro"
    sleepy = random.choice((True, False))

    def turn(self, opponent):
        if not self.sleepy:
            self.score += 2
        self.sleepy = not self.sleepy


class HealerCharacter(Character):
    name = "Healer"

    def turn(self, opponent):
        opponent.score -= 1


class MageCharacter(Character):
    name = "Mage"
    power = 0

    def turn(self, opponent):
        self.power += 1
        # -score makes them smarter, +++winrate
        if self.power >= opponent.goal_score - self.score:
            self.score += self.power
            self.power = 0


class GamblerCharacter(Character):
    name = "Gambler"
    odds = [-4, -2, 0, 2, 4, 6]  # +6 total advantage / 6 slots = 1/turn

    def turn(self, opponent):
        self.score += random.choice(self.odds)


class TaxCharacter(Character):
    name = "Tax"
    rate = .1

    def turn(self, opponent):
        self.score += self.rate * opponent.goal_score

##############################################################################


class Game():
    goal_score = 10
    turn_max = 1000  # prevent infinite games - most won't got this long

    def __init__(self, p1, p2):
        self.turn_curr = 0
        self.p1 = p1
        self.p2 = p2

    def play(self):
        while self.p1.score < self.p2.goal_score and \
                self.p2.score < self.p1.goal_score and \
                self.turn_curr < self.turn_max:
            self.turn_curr += 1
            self.p1.turn(self.p2)
            self.p2.turn(self.p1)

        if self.p1.score >= self.p2.goal_score and \
                self.p2.score >= self.p1.goal_score:
            return 0
        elif self.p1.score >= self.p2.goal_score:
            return 1
        elif self.p2.score >= self.p1.goal_score:
            return -1
        else:
            return 0


class GameManager():
    characters = [
            Character, AggroCharacter, GamblerCharacter,
            HealerCharacter, JackpotCharacter, TankCharacter,
            TaxCharacter, MageCharacter, VampCharacter
            ]

    def __init__(self):
        print(
                ("{:10}|" + ("{:4}|"*len(self.characters))).format(
                    "", * [str(char())[:4] for char in self.characters]
                    )
        )

        overall_score = defaultdict(int)

        # Play each AI against each other AI. player1 has first turn advantage,
        # but each AI also takes a turn as player2 in each matchup,
        # so there's no overall order advantage.
        print("----------|" + "----|" * len(self.characters))
        for player1 in self.characters:
            record = []
            for player2 in self.characters:
                wins = 0
                for i in range(10):
                    wins += Game(player1(), player2()).play()
                record.append(wins)
                overall_score[player1] += wins
                overall_score[player2] -= wins
            print(
                    ("{:10}|" + ("{:4}|"*len(self.characters))).format(
                        player1.name,
                        * record
                    )
                )

        # Print final data
        print("-----------" + "-----" * len(self.characters))
        print("Name      |Total Score")
        print("----------|-----------")

        scores = sorted(
                overall_score.items(),
                key=lambda keyval: -keyval[1]
            )
        for player in scores:
            print("{:10}|{}".format(player[0].name, player[1]))


GameManager()
