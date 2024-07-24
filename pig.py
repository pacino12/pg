# turn rool the dice and you get a number
import random


def roll():
    min_value = 1
    max_value = 6
    # the dice will be rolled between 1 wnd 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    # the reason for this is to keep asking the user to type a selected number
    players = input("Enter the number of players(1-4): ")
    if players.isdigit:
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 1 to 4")

    else:
        print("Invlid input, Try again")


max_score = 50
# put zero inside the list for every single player we have
# list comprehension [expression for item in iterable]
player_score = [0 for _ in range(players)]

print(player_score)
while max(player_score) < max_score:
    for player_idx in range(players):
        print("player number", player_idx + 1, "Turn has just started! \n")
        print("Your total Score is is:", player_score[player_idx], "\n")
        current_score = 0
        while True:
            current_score = 0
            should_roll = input("would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is:", current_score)
        player_score[player_idx] += current_score
        print("Your tota score is: ", player_score[player_idx])
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("player number", winning_idx + 1,
      "core of: ", max_score)
