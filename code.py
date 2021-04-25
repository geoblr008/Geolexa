import random

home = input("enter your name: ")  
want = input(f"{home} what do you want: ")
if want == "riddle"or want == "Riddle" or want == "RIDDLE" :
    riddle=["what goes up when rain comes down ?","How many months of the year have 28 days?", "What has hands and a face, but can’t hold anything or smile?"," If you don’t keep me, I’ll break. What am I?"]
    num = random.randint(0, 3)
    print(riddle[num])
    solution=["umbrella","12","clock","promise."]
    answer=input("your answer pls ")
    if (answer == solution[num]) :
        print(f"{home} your answer is correct")
    else:
        print (f"{home} your answer is wrong")
if want == "joke"or want == "JOKE" or want == "Joke": 
    joke=["Knock! Knock! Who’s there? Control Freak. Con… OK, now you say, “Control Freak who?” ","Did you hear about the actor who fell through the floorboards? He was just going through a stage."]
    num = random.randint(0, 1)
    print(joke[num])
