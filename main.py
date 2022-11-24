import random
from steps import Game

randomNumberEven = random.randint(2,20)
randomNumber = 0
if randomNumberEven % 2 == 0:
    randomNumber = randomNumberEven

eg1 = 10 + randomNumber
eg2 = 16 + randomNumber

div_eg1 = round(eg1/2)
div_eg2 = round(eg2/2)
input_string = "INPUT (Hit Enter)"

funcs = Game(
    eg1 = eg1,
    eg2 = eg2,
    div_eg1 = div_eg1,
    div_eg2 = div_eg2,
    input_string = input_string,
    random_number = randomNumber
)

funcs.run_game()