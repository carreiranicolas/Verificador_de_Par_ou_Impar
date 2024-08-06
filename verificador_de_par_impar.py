while True:

    try:
        numero = int(input("Informe um número que você quer verificar: "))
        if numero % 2 == 0:
            print("O número é PAR!")
        else:
            print("O número é IMPAR!")
        break
    
    except:
        print("Erro na entrada de dados. Por favor, informe um número inteiro.")

