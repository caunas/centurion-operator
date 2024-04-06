#importando dependencias
import os
from time import sleep

#clear the terminal command
def clear_terminal():
    os.system('cls' if os.name == 'nt' else clear)

def tittle():
    print("""
   _____ ______ _   _ _______ _    _ _____  _____ ____  _   _     ____  _____  ______ _____        _______ ____  _____  
  / ____|  ____| \ | |__   __| |  | |  __ \|_   _/ __ \| \ | |   / __ \|  __ \|  ____|  __ \    /\|__   __/ __ \|  __ \ 
 | |    | |__  |  \| |  | |  | |  | | |__) | | || |  | |  \| |  | |  | | |__) | |__  | |__) |  /  \  | | | |  | | |__) |
 | |    |  __| | . ` |  | |  | |  | |  _  /  | || |  | | . ` |  | |  | |  ___/|  __| |  _  /  / /\ \ | | | |  | |  _  / 
 | |____| |____| |\  |  | |  | |__| | | \ \ _| |_ |__| | |\  |  | |__| | |    | |____| | \ \ / ____ \| | | |__| | | \ \ 
  \_____|______|_| \_|  |_|   \____/|_|  \_\_____\____/|_| \_|   \____/|_|    |______|_|  \_\_/    \_\_|  \____/|_|  \_\ 
  
  V. 0.2.1""")

def initialize():
    clear_terminal()
    tittle()
    print("Iniciando sistema..."), sleep(2), print("OK \n")
    input("Pressione qualquer tecla para começar...")