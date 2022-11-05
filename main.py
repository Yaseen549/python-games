import random
randomNumber = random.randint(2,20)
randomInt = 0
if randomNumber % 2 == 0:
    randomInt = randomNumber

inputStr = "INPUT (Hit Enter)"

print("Guess a number between 1 to 10: ")
print("Ex: 5\nEx 2: 8")
input(inputStr)

print("----------------------------------")
print("Multiply with 2")
print("Ex: if guess os 5 then 5x2=10")
print("Ex: if guess os 5 then 8x2=16")
input(inputStr)

