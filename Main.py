import os

from database import Banco
from gerador import GeradorSenha


def limpar():

    os.system("cls" if os.name == "nt" else "clear")


def menu():

    print("=" * 40)
    print("gerenciador de senhas")
    print("=" * 40)
    print("1 - Adicionar conta")
    print("2 - Buscar conta")
    print("3 - Listar contas")
    print("4 - Alterar senha")
    print("5 - Excluir conta")
    print("6 - Gerar senha")
    print("7 - Sair")
    print("=" * 40)


def main():

    banco = Banco()

    gerador = GeradorSenha()

    while True:

        limpar()

        menu()

        opcao = input("Escolha: ")

        if opcao == "1":

            site = input("Site: ")

            usuario = input("Usuário: ")

            senha = input("Senha: ")

            banco.adicionar(site, usuario, senha)

            input("\nConta salva! ENTER...")

        elif opcao == "2":

            site = input("Pesquisar site: ")

            banco.buscar(site)

            input("\nENTER...")

        elif opcao == "3":

            banco.listar()

            input("\nENTER...")

        elif opcao == "4":

            site = input("Site: ")

            senha = input("Nova senha: ")

            banco.alterar(site, senha)

            input("\nAtualizado! ENTER...")

        elif opcao == "5":

            site = input("Site: ")

            banco.excluir(site)

            input("\nRemovido! ENTER...")

        elif opcao == "6":

            tamanho = int(input("Quantidade de caracteres: "))

            print()

            print(gerador.gerar(tamanho))

            input("\nENTER...")

        elif opcao == "7":

            print("Até logo!")

            break

        else:

            print("Opção inválida.")

            input("\nENTER...")


if __name__ == "__main__":

    main()
