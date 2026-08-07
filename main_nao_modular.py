def menu_principal(saldo):
    while True:
        print("escolha a opção")
        print("1- Adicionar")
        print("2- Subtrair")
        print("3- ver dados")
        print("4- sair")

        match input("Digite a opção desejada: "):
            case "1":
                print("adicionar")
                saldo = requisitar_adicao(saldo)
            case "2":
                print("subtrair")
                saldo = requisitar_subtracao(saldo)
            case "3": 
                print("ver dados")
                print(saldo)
            case "4":
                print("sair")
                break

def requisitar_adicao(saldo):
    print("Requisitando movimentação...")
    valor = float(input("Digite o valor a ser adicionado: "))
    saldo = adicionar(saldo, valor)
    return saldo

def requisitar_subtracao(saldo):
    print("Requisitando movimentação...")
    valor = float(input("Digite o valor a ser subtraído: "))
    saldo = subtrair(saldo, valor)
    return saldo

def adicionar(saldo, valor):
    saldo += valor
    print(f"Novo saldo: {saldo}")
    return saldo

def subtrair(saldo, valor):
    saldo -= valor
    print(f"Novo saldo: {saldo}")
    return saldo

def main():
    saldo = 0.0
    menu_principal(saldo)

if __name__ == "__main__":
    main()