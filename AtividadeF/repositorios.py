from repositorio import *


class Repositorios:
    def __init__(self, repositorios=[]):
        self.repositorios = repositorios

    def criar_repositorio(self):
        while True:
            nome = input("\nDigite o nome do repositório que deseja criar: ")

            repositorio_existe = False
            for item_repositorio in self.repositorios:
                if item_repositorio.nome == nome:
                    repositorio_existe = True
                    break

            if repositorio_existe:
                print("\nO repositório com esse nome já existe! Escreva outro nome.")
                continue

            repositorio = Repositorio(nome)
            self.repositorios.append(repositorio)

            print("\n\033[1;32;mRepositório Criado com Sucesso!")
            break

    def listar_repositorios(self):
        print("\033[1;36;m\nRepositórios:\033[m")
        [print(repositorio.nome) for repositorio in self.repositorios]

    def acessar_repositorio(self):
        while True:
            if not self.repositorios:
                print("\nSem repositórios, é necessário criar um primeiro!")
                return None

            nome = input("\nDigite o nome do repositório que deseja acessar: ")
            repositorio_existe = False

            for item_repositorio in self.repositorios:
                if item_repositorio.nome == nome:
                    repositorio_existe = True
                    repositorio = item_repositorio
                    break

            if not repositorio_existe:
                print("\nEsse nome de repositório não existe! Digite outro nome.")
                continue

            return repositorio

    def verificar_vinculo(self):
        pass
