try:
    divisão = 10 / 0
    print(divisão)
except:
    print('''não foi possível realizar essa operação''')
        
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("por favor, não ultilize zeros!!")
    except:
        print("\033[91m algo de errado...")
    else:
        print(f"seu resultado é {result}")
    finally:
        print("\033[92m vamos de novo?")
divide(13,0)

import random
value = random.randint(0, 3)

match value:
    case 0:
         print("zero!")
    case 1:
        print("um!")
    case 2:
         print("dois!")
    case _:
         print("except")
         