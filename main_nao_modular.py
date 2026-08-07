def menu_principal(saldo_atual):
    while True:
        print("escolha a opção")
        print("1- Adicionar")
        print("2- Subtrair")
        print("3- ver dados")
        print("4- sair")

        match input("Digite a opção desejada: "):
            case "1":
                print("adicionar")
                saldo_atual = requisitar_adicao(saldo_atual)
            case "2":
                print("subtrair")
                saldo_atual = requisitar_subtracao(saldo_atual)
            case "3": 
                print("ver dados")
                print(saldo_atual)
            case "4":
                print("sair")
                break

def requisitar_adicao(saldo_atual):
    print("Requisitando movimentação...")
    valor_informado = float(input("Digite o valor a ser adicionado: "))
    saldo_atualizado = adicionar(saldo_atual, valor_informado)
    return saldo_atualizado

def requisitar_subtracao(saldo_atual):
    print("Requisitando movimentação...")
    valor_informado = float(input("Digite o valor a ser subtraído: "))
    saldo_atualizado = subtrair(saldo_atual, valor_informado)
    return saldo_atualizado

def adicionar(saldo_atual, valor_informado):
    saldo_atual += valor_informado
    print(f"Novo saldo: {saldo_atual}")
    return saldo_atual

def subtrair(saldo_atual, valor_informado):
    saldo_atual -= valor_informado
    print(f"Novo saldo: {saldo_atual}")
    return saldo_atual

def main():
    saldo_inicial = 0.0
    menu_principal(saldo_inicial)

if __name__ == "__main__":
    main()