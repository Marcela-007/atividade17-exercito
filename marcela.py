# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
print("Alistamento militar")
idade = int(input("Digite o ano do seu nascimento: "))
anoatual = int(input("Digite o ano atual: "))
if anoatual-idade > 18:
  print(f"Você passou da idade de alistar, por favor procure um quartel para se alistar. Você está atrasado há {(anoatual-idade)-18} ano(s)") 
elif anoatual-idade < 18:
  print(f"Você não possui a idade certa para se alistar.Tempo faltante para o eu alistamento = {18-(anoatual-idade)} ano(s)")
else:
  print("Você está na idade certa de se alistar!")