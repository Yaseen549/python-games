import random

randomNumber = random.randint(2, 20)
randomInt = 0
if randomNumber % 2 == 0:
    randomInt = randomNumber

inputStr = "\nINPUT (Hit Enter)"

questions = [
    "Guess a number between 1 to 10: ",
    "Multiply with 2",
    f"Add {randomInt} to it.",
    "Divide it by 2",
    "Subtract the number you guessed from the result",
    f"Your answer would be: {round(randomInt / 2)}"
]

print("----------------------------------")
# execute = methods_list[position](randomInt)
# step_by.step_1()
input(inputStr)


def __init__(self):
    pass


def step_1(self):
    print("Ex: 5")


def step_2(self):
    print("Ex: if guess is 5 then 5x2=10")


def step_3(self, randomInt):
    eg1 = 10 + randomInt
    print(f"Ex: 10 + {randomInt} = ", eg1)


def step_4(self):
    div_eg1 = round(eg1 / 2)
    print(f"Ex: {eg1}/2 = {div_eg1}")


def step_5(self):
    print(f"Ex: if guess is 5 then subtract it {div_eg1}-5")


def result(self):
    print()


methods_list = [step_1(), step_2(), step_3(), step_4(), step_5(), result()]
