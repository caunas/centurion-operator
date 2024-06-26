#import modules
from modules import scripts as scr, resources as rsc
from time import sleep

rsc.initialize()
rsc.clear_terminal()

while True:
    print("""
          1. Calcular dano
          2. Porcentagem simples
          3. Role um dado
          
          0. Sair
""")
    
    request = int(input("Selecione uma opção: "))
    rsc.clear_terminal()
    
    #calc dano
    if request == 0:
        exit()
    elif request == 1:
        dmg_inject = float(input("Dano aplicado: "))
        dmg_block = float(input("Armadura ou Resistência Mágica: "))
        dmg_bypass = float(input("Letalidade ou Penetração Mágica: "))
        
        response = scr.calcDmg(dmg_inject, scr.calcArmor(dmg_block - dmg_bypass))
        
        print(f"Dano total recebido: {response}")
        input("Pressione qualquer tecla para continuar...")
        
        rsc.clear_terminal()
        
    #calcular porcentagem    
    elif request == 2:
        total_qtd = float(input("Insira a quantidade a ser calculada: "))
        part = float(input(f"Quantos porcento de {total_qtd} você quer calcular? "))
        
        response = scr.percent(part, total_qtd)
        
        print(f"{part}% de {total_qtd} é igual a {response}")
        input("Pressione qualquer tecla para continuar...")
        
        rsc.clear_terminal()
    
    #roll dice
    elif request == 3:
        dice_rolls = int(input("Quantas vezes quer rolar o dado? "))
        while True:
            dice_sides = int(input("Quantos lados o dado tem? "))
            if(dice_sides % 2 != 0):
                print("Erro: Número de dados inválido. Tente Novamente.")
                continue
            else:
                break
        
        response = scr.rollDice(dice_rolls, dice_sides)
        
        while True:
            dmg_request = input("Deseja seguir para calcular o dado de dano (Y/N)? ")
            dmg_request = dmg_request.lower()
            if dmg_request == 'y':
                
                dmg_inject = response
                
                print(f'\nDano aplicado: {dmg_inject}')
                
                dmg_block = float(input("Armadura ou Resistência Mágica: "))
                dmg_bypass = float(input("Letalidade ou Penetração Mágica: "))
                
                response = scr.calcDmg(dmg_inject, scr.calcArmor(dmg_block - dmg_bypass))
                
                print(f"\nDano total recebido: {response} \n")
                input("Pressione qualquer tecla para continuar...")
                
                
                break
            elif dmg_request == 'n':
                break
            else:
                print(f"Opção Inválida, tente novamente.")
                continue
            
        rsc.clear_terminal()
        
    #error 01
    else:
        print(f"Erro, a opção de número {request} não existe.")
        
        print("Retornando ao menu principal...")
        sleep(2)
        rsc.clear_terminal()
