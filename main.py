import random

def select_x():
    while True:
        x_input = input("Select x: ").lower()
        if x_input == "a":
            x_int = 1
            return x_int
        elif x_input == "b":
            x_int = 2
            return x_int
        elif x_input == "c":
            x_int = 3
            return x_int
        else:
            print("Invalid input")

def select_y():
    while True:
        y_input = input("Select y: ")
        if y_input == "1" or y_input == "2" or y_input == "3":
            y_int = int(y_input)
            return y_int
        else:
            print("Invalid input")

def check_win(game_matrix):
    if game_matrix[1] == ["1", "o", "o", "o"] or game_matrix[2] == ["2", "o", "o", "o"] or game_matrix[3] == ["3", "o", "o", "o"]:
        return True
    elif game_matrix[1][1] == "o" and game_matrix[2][1] == "o" and game_matrix[3][1] == "o":
        return True
    elif game_matrix[1][2] == "o" and game_matrix[2][2] == "o" and game_matrix[3][2] == "o":
        return True
    elif game_matrix[1][3] == "o" and game_matrix[2][3] == "o" and game_matrix[3][3] == "o":
        return True
    elif game_matrix[1][1] == "o" and game_matrix[2][2] == "o" and game_matrix[3][3] == "o":
        return True
    elif game_matrix[3][1] == "o" and game_matrix[2][2] == "o" and game_matrix[1][3] == "o":
        return True
    else:
        return False

def check_lose(game_matrix):
    if game_matrix[1] == ["1", "x", "x", "x"] or game_matrix[2] == ["2", "x", "x", "x"] or game_matrix[3] == ["3", "x", "x", "x"]:
        return True
    elif game_matrix[1][1] == "x" and game_matrix[2][1] == "x" and game_matrix[3][1] == "x":
        return True
    elif game_matrix[1][2] == "x" and game_matrix[2][2] == "x" and game_matrix[3][2] == "x":
        return True
    elif game_matrix[1][3] == "x" and game_matrix[2][3] == "x" and game_matrix[3][3] == "x":
        return True
    elif game_matrix[1][1] == "x" and game_matrix[2][2] == "x" and game_matrix[3][3] == "x":
        return True
    elif game_matrix[3][1] == "x" and game_matrix[2][2] == "x" and game_matrix[1][3] == "x":
        return True
    else:
        return False

def check_spaces(game_matrix):
    to_check = " "
    found = False

    for check in game_matrix:
        if to_check in check:
            found = True
            break

    return found

def get_choice():
    user_choice = input("Would you like to play again? (y/n): ")
    while True:
        if user_choice == "y".lower():
            return 1
        elif user_choice == "n".lower():
            return 2
        else:
            print("Invalid input")

wins = 0
loses = 0
draws = 0

while True:
    matrix = [
        ["/", "A", "B", "C"],
        ["1", " ", " ", " "],
        ["2", " ", " ", " "],
        ["3", " ", " ", " "]
    ]

    turn = 0

    for a in matrix:
        print(a)

    # choose who go first
    start = random.randint(0, 1)
    if start == 1:
        print("You go first")
        print()
        turn = 1
    else:
        print("PC go first ")
        print()

    # game
    while True:
        win = check_win(matrix)
        lose = check_lose(matrix)
        spaces = check_spaces(matrix)

        if turn == 1 and win == False and lose == False and spaces:
            print("Your turn")

            while True:
                print("Select your move")
                x = select_x()
                y = select_y()

                if matrix[y][x] == " ":
                    matrix[y][x] = "o"
                    for a in matrix:
                        print(a)
                    print()
                    turn = 0
                    break
                else:
                    print(f"{x},{y} is already occupied")
                    print("Choose another space")


        elif turn == 0 and win == False and lose == False and spaces:
            print("PC Turn")

            while True:
                rand_x = random.randint(1, 3)
                rand_y = random.randint(1, 3)

                if matrix[rand_y][rand_x] == " ":
                    matrix[rand_y][rand_x] = "x"
                    for a in matrix:
                        print(a)
                    print()
                    turn = 1
                    break
                else:
                    pass

        if not spaces:
            print("No spaces left")
            draws += 1
            break

        if win:
            print("You win")
            wins += 1
            break
        elif lose:
            print("You lose")
            loses += 1
            break

    choice = get_choice()
    if choice == 1:
        print()
        print(f"Wins: {wins}")
        print(f"Loses: {loses}")
        print(f"Draws: {draws}")
        print()
    if choice == 2:
        print("Thanks for playing")