# get guess
import random
def get_guess():
    return list(input("what is your guess: "))

# generate computer code
def generate_code():
    digits =[str(num) for num in range(10)]

    #shuffle digits
    random.shuffle(digits)
    #grab first three
    return digits[:3]

#generate the clues

def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"
    
    clues = []
 
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match") # match means correct numberr in correct position
        elif num in code:
            clues.append("close") # correct nmumber in wrong position
    
    if clues == []:
        return ["Nope"] # havnt guess any number correctly
    else:
        return clues



#run game logic
print ("welcome code breaker")
secret_code = generate_code()
clue_report =[]

while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print ("here is te result of your guess: ")
    for clue in clue_report:
        print(clue)

