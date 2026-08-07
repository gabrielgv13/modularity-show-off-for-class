from dinheiro.requisitar_movimentacao import processar_adicao, processar_subtracao

def menu_principal(saldo):
    while True:
        print("escolha a opção")
        print("1- Adicionar")
        print("2- Subtrair")
        print("3- ver dados")
        print("4- sair")

        match input("Digite a opção desejada: "):
            case "1":
                saldo = solicitar_adicao(saldo)
            case "2":
                saldo = solicitar_subtracao(saldo)
            case "3": 
                print("ver dados")
                print(saldo)
            case "4":
                print("sair")
                break


def solicitar_adicao(saldo):
    valor = float(input("Digite o valor a ser adicionado: "))
    saldo_atualizado = processar_adicao(saldo, valor)
    print("Valor adicionado.")
    print(f"Novo saldo: {saldo_atualizado}")
    return saldo_atualizado


def solicitar_subtracao(saldo):
    valor = float(input("Digite o valor a ser subtraído: "))
    saldo_atualizado = processar_subtracao(saldo, valor)
    print("Valor subtraído.")
    print(f"Novo saldo: {saldo_atualizado}")
    return saldo_atualizado