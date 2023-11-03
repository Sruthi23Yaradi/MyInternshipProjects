print("The game is as follows")
print()
print("You are exploring a Jungle with no food and water. You come across a lot of circumstances where you are given an option to choose. The winning or losing of the game is decided based on the player's survival. So you need to choose the options that increases the survival chances")
print()

ans= input("Do you want to play this text adventure game? [yes/no]\t")
if ans == "yes":
    print("\nThat's Great!!\n")
    print()
    opt = input("You saw a tree full of fruits.\nDo you want to take them or not? [yes/no]\t")
    if opt == "yes":
        print("That's a great choice")
        print()
    else:
        print("It's okay! You can continue your journey")
        print()
    opt1 = input("You have come across a lake full of fresh water.\nDo you want to take them or not? [yes/no]\t")
    if opt1== "yes":
        print("That's a great choice")
        print()
        opt2= input("Hey! There's a wild horse.\nDo you want to use it in exploration?[yes/no]\t")
        if opt2 == "yes":
            print("You'll be collided with the trees in the forest. You lose \U0001F62D")
            print()
        else:
            print("You can continue your exploration")
            print()
            opt3=input("Oh no! There's a bear coming on your way \U0001F972. Do you get panic or act as dead? [panic/act]\t")
            if opt3 == "panic":
                print("Oh! You lose \U0001F62D")
            else:
                print("That's great!!! Keep going")
                print()
                print("You reached the danger zone")
                opt4= input("Do you want to explore the cave or the jungle? [cave/jungle]\t")
                if opt4 == "cave":
                    print("You win \U0001F929")
                else:
                    print("The wild animals attack. You lose \U0001F62D")
    else:
        print("It's okay! You can continue your journey")
        print()
    if opt == "no" and opt1 == "no":
        print("You lose due to lack of energy \U0001F62D")
        print()
    
    
    

else:
    print("But this is really an awesome game. Give it a try!")
