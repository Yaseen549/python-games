
class Game:
    def __init__(self, eg1, eg2, div_eg1, div_eg2, input_string, random_number):
        self.eg1 = eg1
        self.eg2 = eg2
        self.div_eg1 = div_eg1
        self.div_eg2 = div_eg2
        self.input_string = input_string
        self.randomNumber = random_number

    def step1(self):
        print("Guess a num b/w 1 to 10")
        print("Ex: 5")

    def step2(self):
        print("Multiply with 2")
        print("Ex: if guess is 5 then 5x2=10")

    def step3(self):
        print(f"Add {self.randomNumber} to it.")
        print(f"Ex: 10 + {self.randomNumber} = ", self.eg1)

    def step4(self):
        print("Divide it by 2")
        print(f"Ex: {self.eg1}/2 = {self.div_eg1}")

    def step5(self):
        print("Subtract the number you guess with the result")
        print(f"Ex: if guess is 5 then subtract it {self.div_eg1}-5")

    def result(self):
        print(f"your answer would be: {round(self.randomNumber/2)}")

    funcs = [step1, step2, step3, step4, step5]

    def run_game(self):
        for n in range(0, len(self.funcs)):
            self.funcs[n](self)
            input(self.input_string)
            print("-------------------")
        self.result()
