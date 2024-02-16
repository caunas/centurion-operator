#import dependencies
from random import randint
from time import sleep

#simple percent
def percnt(part, total_qtd):
    result = (part / 100) * total_qtd
    
    return round(result)

#percentage of damage reduct
def calcArmor(armor):
    shield = (armor / (armor + 100)) * 100
    
    return round(shield)

#calc the final damage, require calcArmor
def calcDmg(dmg_positive, dmg_negative):
    damage = dmg_positive - ((dmg_negative / 100) * dmg_positive)
    
    return round(damage)

def rollDice(times_roll, dice_sides):
    print(f"Rolando {times_roll}d{dice_sides}... \n")
    
    sleep(1)
    
    dice_sum = 0
    
    for i in  range(times_roll, 0, -1):
        dice_result = randint(0, dice_sides)
        dice_sum = dice_sum + dice_result
        print(dice_result)
    
    print('\n')
    print(f'Soma dos dados: {dice_sum}')
    
    return dice_sum