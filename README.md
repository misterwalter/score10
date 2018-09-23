# score10
A simple game design experiment about the difficulty of balancing allegedly equal characters.

# The Game
This game is played automatically by very simple characters. By default, each must score 10 points to win. Both take turns taking an action, and then the game checks to see if either has enough points to win. If one does, that character wins. Otherwise, another turn is played.

# The Characters
The characters are all supposedly equivalent to the base Character, who scores one point every turn, and takes 10 points to beat. However, there is a lot of variety in terms of what characters actually do. The Gambler grants itself a random number of points each turn, and sometimes gives itself negative points. The Healer takes a point away from the other character instead of scoring anything itself. The real fun comes in understanding why each character performs the way that it does against the others.

While I generally value proper balance in the games I make and play, it's not a goal of mine to make this a perfectly balanced setup. It's more of an essay written in Python about how massively unbalanced seemingly equal things can be.
