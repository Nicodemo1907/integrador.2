import os
def print_number(n):
   os.system('cls' if os.name=='nt' else 'clear')
   print(n)
n = 0
while n < 50:
   input('Presione n para continuar')
   print_number(n)
   n += 1
