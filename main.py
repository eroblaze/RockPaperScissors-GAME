# This is a rock, paper, scissors game!!!
import random as r, sys
print("""\
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
""")
wins = 0
losses = 0
ties = 0
par = ['ROCK', 'PAPER', 'SCISSORS']
while True:
    move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: \n").lower()
    if move != 'p' and move != 'r' and move != 's' and move != 'q':
        print("Invalid input!")
        print()
    if move == 'r':
        print("ROCK versus....")
        res = r.randrange(0, 3)
        ran = par[res]
        print(ran)
        if ran == 'ROCK':
            print('It is a tie!')
            ties += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        elif ran == 'PAPER':
            print('You lose!')
            losses += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        else:
            print('You win!')
            wins += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()

    if move == 'p':
        print("PAPER versus....")
        res = r.randrange(0, 3)
        ran = par[res]
        print(ran)
        if ran == 'ROCK':
            print('You win!')
            wins += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        elif ran == 'SCISSORS':
            print('You lose!')
            losses += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        else:
            print('it is a tie!')
            ties += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()

    if move == 's':
        print("SCISSORS versus....")
        res = r.randrange(0, 3)
        ran = par[res]
        print(ran)
        if ran == 'SCISSORS':
            print('It is a tie!')
            ties += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        elif ran == 'ROCK':
            print('You lose!')
            losses += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()
        else:
            print('You win!')
            wins += 1
            print(wins, 'Wins, ', losses, ' Losses, ', ties, ' Ties')
            print()

    if move == 'q':
        print("Thank You for playing with us!")
        sys.exit()
