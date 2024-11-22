
import random
human_choice = int(input("enter your choice :type 0 for rock,1 for paper ,2 for scissors."))
computer_choice=random.randint(0,2)
print("human_choice ")
print("computer_choice")
if computer_choice==human_choice:
    print("it's a draw")
elif computer_choice > human_choice:
    print("you lose")
elif human_choice > computer_choice:
    print("you win")
elif computer_choice==0 and human_choice==2:
    print("you lose")
elif human_choice==0 and computer_choice==2:
    print("you win")
