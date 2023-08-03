saldo = 0 #Variável inteira que contém o total de saldo do cliente
numero_de_saques = 0 #Variável inteira contadora do número de saques feito pelo cliente
extrato = [] #lista que mantém todas as operações feitas pelo cliente

if __name__ == "__main__":
    while True: #Inicio do menu
        print("""
========== Menu =========
[0] -> Depositar
[1] -> Sacar
[2] -> Visualizar extrato
[3] -> Sair
=========================""") #Fim do menu
        operacao = int(input("Operação desejada: ")) #Solicitação de qual operação realizar
        if operacao == 0: #Operação de depósito
            aux = int(input("Por favor, informe o quanto deseja depositar: R$"))
            if aux < 0:
                print("Operação inválida!")
            else:
                saldo += aux
                extrato.append(("Depósito", aux)) #Atualização do extrato
        elif operacao == 1: #Operação de saque
            if numero_de_saques < 3:
                aux = int(input("Por favor, informe o quanto deseja sacar: R$"))
                if aux > 500:
                    print("Saque desejado ultrapassou o limite (R$500)!")
                elif aux < 0:
                    print("Operação inválida!")
                elif aux <= saldo:
                    saldo -= aux
                    extrato.append(("Saque", aux)) #Atualização do extrato
                    numero_de_saques += 1
                else:
                    print("Saldo insuficiente para saque! Por favor, deposite mais saldo.")
            else:
                print("Limite diário de saques atingido! Por favor, solicite outra operação.")
        elif operacao == 2: #Operação de extrato
            print("========== Extrato ==========")
            for i, op in enumerate(extrato):
                print(f"Operação de {op[0]} - {op[1]} ({i+1})")
            print("=============================")
            print("Saldo atual = R${:.2f}".format(saldo))
        elif operacao == 3: #Operação de saída
            break
        else:
            print("Operação inválida! Tente novamente.")
    print("Sistema encerrado com sucesso!")