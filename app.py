import os

restaurantes = ["Pizza", "sushi"]

def exibir_nome_do_programa():
    print('''
░█████╗░██╗░░██╗███████╗██╗██████╗░██╗███╗░░██╗██╗░░██╗░█████╗░  ██████╗░░█████╗░███╗░░░███╗
██╔══██╗██║░░██║██╔════╝██║██╔══██╗██║████╗░██║██║░░██║██╔══██╗  ██╔══██╗██╔══██╗████╗░████║
██║░░╚═╝███████║█████╗░░██║██████╔╝██║██╔██╗██║███████║██║░░██║  ██████╦╝██║░░██║██╔████╔██║
██║░░██╗██╔══██║██╔══╝░░██║██╔══██╗██║██║╚████║██╔══██║██║░░██║  ██╔══██╗██║░░██║██║╚██╔╝██║
╚█████╔╝██║░░██║███████╗██║██║░░██║██║██║░╚███║██║░░██║╚█████╔╝  ██████╦╝╚█████╔╝██║░╚═╝░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝\n
''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    #os - faz com que, ao clicar 4 (finalizar programa) o terminal seja limpo
    os.system('cls')
    print("Finalizando app\n")

def Opcao_invalida():
    print("Opçaõ inválida\n")
    input("Precione qualquer tecla para voltar ao meno principal: ")
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastro de novos restaurantes\n ")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("\nPrecione qualquer tecla para voltar ao meno principal: ")
    main()

def listar_restaurantes():
    os.system('cls')
    print("Lista de restaurantes\n")

    for restaurante in restaurantes:
        print(f".{restaurante}")

    input("\nPrecione qualquer tecla para voltar ao meno principal: ")
    main()

def escolher_opcaos():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            Opcao_invalida()
    except:
        Opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcaos()



if __name__ == '__main__':
    main()