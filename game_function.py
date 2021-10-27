def gamefunction():
    choice = ["rock" "paper" "scissor"]
    ch = True
    while (ch == True):
        p1 = input("Player 1 choice")
        p2 = input("Player 2 choice ")
        if (p1 != p2) and (p1 in choice) and (p2 in choice):
            if (p1 == "rock" and p2 == "scissor") or (p1 == "paper" and p2 == "rock") or (
                    p1 == "scissor" and p2 == "paper"):
                print("Congratulations !!! Player 1 won")
            else:
                print("Congratulations !!! Player 2 won")
            new_game = input("Do you want to start a new game? (y/n):")
            if new_game == "y":
                ch = True
            else:
                ch = False
        elif (p1 == p2):
            print("It is a tie")
        else:
            print("Enter the choice properly ")
            pass


gamefunction()

