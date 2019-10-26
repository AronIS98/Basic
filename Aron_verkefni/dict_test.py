# The implementation of Dice goes here
import random
class Dice:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        self.rolled = random.randint(1,self.sides)
        return self.rolled

    def __add__(self,param_Dice):
        new_dice = Dice(int(self.sides)+int(param_Dice.sides))
        new_dice.rolled = self.rolled + param_Dice.rolled
        return new_dice

def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()