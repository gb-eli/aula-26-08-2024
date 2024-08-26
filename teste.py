import time

tempo = 1;

# aqui fica as funções 

def sauda():
    print("Olá")

    nameuser = input("Qual o seu nome?")

    print("Bem vindo" + nameuser)


def menu():
    print("Como posso te ajudar?")
    time.sleep(tempo)
    print("1 - Falar com atendente")
    time.sleep(tempo)
    print("2 - Ligar")
    time.sleep(tempo)
    print("3 - Finalizar pedido")

    opcao = int(input("Escolha uma opção"))

    if opcao == 1:
        print("Aguarde, logo voce ser[a atendido]")

    elif opcao == 2:
        print("O número é 08007070")

    elif opcao == 3:
        print("O número é 08007070")

    else:
        print("Opção incorreta!")


sauda()
menu()


        
