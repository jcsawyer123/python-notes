import random

def response(num):
    if num ==  1:
        return 'It is certain'
    elif num == 2:
        return 'It is so'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return "Unsure, try again"
    elif num == 5:
        return "Ask again later"
    elif num == 6:
        return "You need to concentrate and ask again"
    elif num == 7:
        return "No"
    elif num == 8:
        return "Seems unlikely"
    elif num == 9:
        return "Doubtful"

def eightball():
    x = random.randint(1,9)
    print(response(x))

print("Think of a YES or NO question and see what the magic eight ball has to say.")
input()

eightball()