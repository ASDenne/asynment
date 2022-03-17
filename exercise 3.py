import random
def name():
    return input("who are you")
def player_guess():
    print("paper siccors rock")
    guess = input(">>>").lower()
    if guess == "paper":
        return 1
    elif guess == "rock":
        return 2
    else:
        return 3
def computer_guess():
    return random.randint(1,3)
def who_won(Pguess,Cguess):
    if Pguess == Cguess:
        print("this oround was a draw")
        return "n"
    elif Pguess == 3:
        if Cguess == 1:
            print("you lost this round")
            return "c"
        else:
            print("you won this round")
            return "p"

    elif Cguess == 3:
        if Pguess == 1:
            print("this round winner is you")
            return "p"
        else:
            print("you lost to the computer this round")
            return "c"
    elif Cguess > Pguess:
        print("you lost to a robot this round")
        return  "c"
    else:
        print("you win this round")
        return "p"



#main
Player = name()
Pguess = ""
Cguess = ""
Pscore = 0
Cscore = 0
while Cscore != 3 and Pscore != 3:
    Pguess = player_guess()
    Cguess = computer_guess()
    Rwinner = who_won(Pguess, Cguess)
    if Rwinner == "c":
        Cscore += 1
    elif Pscore == "p":
        Pscore += 1
if Cscore > Pscore:
    print(f"{Player} lost")
else:
    print(f"y{Player} won")
