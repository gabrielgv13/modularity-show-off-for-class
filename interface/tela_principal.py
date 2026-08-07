from dinheiro.servico_saldo import processar_adicao, processar_subtracao

def menu_principal(saldo_atual):
    while True:
        print("escolha a opção")
        print("1- Adicionar")
        print("2- Subtrair")
        print("3- ver dados")
        print("4- sair")

        match input("Digite a opção desejada: "):
            case "1":
                saldo_atual = solicitar_adicao(saldo_atual)
            case "2":
                saldo_atual = solicitar_subtracao(saldo_atual)
            case "3": 
                print("ver dados")
                print(saldo_atual)
            case "4":
                print("sair")
                break


def solicitar_adicao(saldo_atual):
    valor_informado = float(input("Digite o valor a ser adicionado: "))
    saldo_atualizado = processar_adicao(saldo_atual, valor_informado)
    print("Valor adicionado.")
    print(f"Novo saldo: {saldo_atualizado}")
    return saldo_atualizado


def solicitar_subtracao(saldo_atual):
    valor_informado = float(input("Digite o valor a ser subtraído: "))
    saldo_atualizado = processar_subtracao(saldo_atual, valor_informado)
    print("Valor subtraído.")
    print(f"Novo saldo: {saldo_atualizado}")
    return saldo_atualizado