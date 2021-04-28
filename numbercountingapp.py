import random
number=random.randint(1,9)
chances=0
print("number between 1-9")
while(chances<5):
    guess=int(input("enter your guess"))
    if guess==number:
        print("you won")
        break
    else:
        print("you lost a chance try again",guess)
    chances+=1
