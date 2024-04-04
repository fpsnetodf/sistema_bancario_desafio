menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ \033[32m{valor:.>36.2f}\033[0;0m\n'

        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))
        if valor > limite or numero_saques >= LIMITE_SAQUES or valor > saldo or valor < 0:
            print("Transação invalida:")
            if valor > limite:
                print(f"O valor solicitado excede o limite de saque: {limite}")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Você excedeu o limite de saques diarios: {LIMITE_SAQUES}")
            elif valor > saldo:
                print(f"O valor solicitado é superior ao seu saldo:")
            elif valor < 0:
                print(f"O valor não pode ser negativo ou nulo")
        else:
            saldo -= valor
            extrato += f'saque:    R$ \033[31m{valor:.>36.2f}\033[0;0m\n'
            numero_saques += 1

    elif opcao == 'e':
        print("=================== Extrato =====================")
        print(extrato)
        print(f"\n\nSeu saldo é: R$ {saldo:.>33.2f}")
        print("=================================================")
    elif opcao == 'q':
        print("Volte sempre!")
        break  
    elif opcao not in 'dseq':
        print("Selecione uma opção valida: ") 
    else: 
        print("opção invalida!")
            