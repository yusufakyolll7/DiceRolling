import random

def roll_dice():
    return random.randint(1,6)

def play_dice_game():
    print("Welcome to the Dice Game!")
    player1 = input("Enter Player 1 name : ")
    player2 = input("Enter Player 2 name : ")

    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(f"\n{player1} rolled a {player1_roll}")
    print(f"\n{player2} rolled a {player2_roll}")

    if player1_roll > player2_roll:
        print(f"\n{player1} wins!")
    elif player2_roll > player1_roll:
        print(f"\n{player2} wins!")
    else:
        print("\nIt is a tie!")

if __name__ == "__main__":
    play_dice_game()