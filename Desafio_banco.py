def depositar(saldo, extrato, /):
    try:
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n=== Depósito no valor de R$ {valor:.2f} realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. Tente novamente. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. Por favor, insira um número. @@@")
        
    return saldo, extrato

def sacar(*, saldo, extrato, numero_saques, limite_saques, limite_valor):
    try:
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite_valor = valor > limite_valor
        excedeu_limite_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print(f"\n@@@ Operação falhou! Saldo insuficiente. Saldo atual: R$ {saldo:.2f} @@@")

        elif excedeu_limite_valor:
            print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite_valor:.2f} por operação. @@@")

        elif excedeu_limite_saques:
            print(f"\n@@@ Operação falhou! Número máximo de {limite_saques} saques diários foi excedido. @@@")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. Por favor, insira um número. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("========================================")

def main():
    menu = """
    =============== MENU ===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ====================================
    => """

    saldo = 0
    limite_valor = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                limite_valor=limite_valor
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("\n@@@ Operação inválida! Por favor, selecione uma das opções do menu. @@@")


main()