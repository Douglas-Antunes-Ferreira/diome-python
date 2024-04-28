print("\nSEJA BEM VINDO!")
#saldação ao clente


menu = """
_____MENU_____\n       
[1]-Depositar
[2]-Sacar
[3]-Extrato
[0]-Sair\n_______________\n=>"""
#abre a aba de menu pra o cliente selecionar a opção


Saldo = 0.0
Limite = 500
Extrato = ""
Numero_de_Saque = 0
LIMITE_DE_SAQUE = 3
#determina as constantes como regra principal do sistema


while True:
#abre o loop do menu

  
  opção = input(menu)  
  if opção == "1":
    print (f"seu saldo atual é: R${Saldo:.2f}")
    valor = float(input("informe o valor a ser depositado: "))
  #se opção igua a um, motra o saldo com duas casas decimais e informe o deposito
  
    
    if valor > 0:
      print(f"\nvalor de R$:{valor:.2f} foi DEPOSITADO com sucesso!")
      print(f"seu saldo atual passou a ser: R${Saldo + valor:.2f}")
    #condição para aceitar somente valores maiores que zero
    

      Saldo += valor
      Extrato += f"deposito: R${valor:.2f}\n"
      #soma o saldo ao valor e leva para o extrato
      
        
    else:
      print("operação invalida, valor inserido negativo ou igual a zero")
    #nao permite valores iguais a zero ou negativos
    
         
  elif opção == ("2"):
    print (f"seu saldo atual é: R${Saldo:.2f}")
    valor= float(input("informe o valor do saque: "))
  #saca o valor
  
    
    if valor < Limite and Numero_de_Saque < LIMITE_DE_SAQUE and valor > 0 and Saldo > valor:
      print(f"\nvalor de: R${valor:.2f} foi SACADO com sucesso! :)")
      print(f"seu saldo atual passou a ser: R${Saldo - valor:.2f}")  
      print(f"\nnumeros de saque nessa operação: {Numero_de_Saque +1} de 3")  
    #condições para que não saque valores miores que limite
    #condições para que o numero de saque não seje maior que o limite de saque
    #condições para que não saque valores menores ou igual a zero
    #condições para que não saque valores maiores que o saldo
    
    
    excedeu_saldo = valor > Saldo 
    excedeu_limite = valor > Limite
    excedeu_saque =Numero_de_Saque >= LIMITE_DE_SAQUE
    #variáveis para as condições de quando o valor for mairo que os saque
    #variáveis para as condições de quando o valor for superior ao limite
    #variáveis para as condições de quando o numero de saque for maior ou igual ao limite de saque
    
    
    if excedeu_saldo:
      print("operação falhou! você não tem saldo suficiente")
      print(f"seu saldo em conta é de: R${Saldo:.2f}")
    #se atingiu a variável (excedeu_saldo) print e mostre o valor do saldo
      
    elif excedeu_limite:
      print("opção falhou! o valor do saque excedeu o limite")
      print(f"seu limite de saque é de: R${Limite:.2f}")
    #se atingiu a variável (excedeu_limite) print e mostre o limite 
      
    elif excedeu_saque:
      print("\nopção falhou! numero maximo de saques excedidos")
      print(f"numeros de saques nessa operação: {Numero_de_Saque}")
      print(f"seu limite de saque é de: {LIMITE_DE_SAQUE} vezes")
    #se atingiu a variável (excedeu saque) print e mostre o numero de saques ate agora e o limite de saque  
        
    elif valor > 0:
      Saldo -= valor
      Extrato += f"saque: R$-{valor:.2f}\n"
      Numero_de_Saque += 1
    #se valor for maior que zero, subtraia do saldo, coloque no extrato, e some mais um no numero de saque
      
    else:
      print("operação falhou! o valor informado é invalido.")
    #se valor for menor ou igual a zero: print  
      
    
  elif opção == "3":
    print("\n=========== EXTRATO============\n")
    print("não foram realizados movimentações." if not Extrato else Extrato)
    print(f"\nsaldo: R${Saldo:.2f}\n")
    print("_____________FIM________________")
  #se opção for exatament igual a três, mostre o extrato
  #motre as movimentações feitas ao longo da operação
  #mostre o saldo atual atualizado, com duas casas decimais
  
    
  elif opção == "0":
    print("\nOBRIGADO POR USAR NOSSO SISTEMA BANCARIO.")
    print("TENHA UM OTIMO DIA!\n")
    print("_________FIM___________\n")
  #seu opção for exatamente igual a zero: print  
  
    break
    #encerra o loop aberto na linha 22
    
  else:
    print("operação inválida! por favor digite somente opções informadas.")      
  #se as opções forem diferentes dos numeros (1, 2, 3 e 0): print 
