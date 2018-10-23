from editordetexto import *
from arquivo import *
from commits import *


class Repositorio:
    def __init__(self, nome, arquivos=[], remoto=[], commits=Commits()):
        self.nome = nome
        self.arquivos = arquivos
        self.remoto = remoto
        self.commits = commits

    def criar_arquivo(self):
        while True:
            nome = input("\nDigite o nome do arquivo que deseja criar(será um arquivo .txt): ")
            if nome[-4::] != ".txt":
                nome += ".txt"

            arquivo_existe = False
            for item_arquivo in self.arquivos:
                if item_arquivo.nome == nome:
                    arquivo_existe = True
                    break

            if arquivo_existe:
                print("\nO arquivo com esse nome já existe! Escreva outro nome.")
                continue
            break

        print("Digite o conteúdo do texto (terminando com uma linha apenas com um S):")
        conteudo = []
        while True:
            linha = input()
            if linha == "S":
                break
            conteudo.append(linha)

        arquivo = Arquivo(nome, conteudo)
        self.arquivos.append(arquivo)

    def listar_arquivos(self):
        print("\nArquivos:")
        [print(arquivo.nome) for arquivo in self.arquivos]

    def selecionar_arquivo(self):
        while True:
            arquivo_existe = False
            if not self.arquivos:
                print("Não há nenhum arquivo nesse repositório!")
                break
            nome_arquivo = input("Digite o nome do arquivo: ")
            for arquivo in self.arquivos:
                if nome_arquivo == arquivo.nome:
                    arquivo_selecionado = arquivo
                    arquivo_existe = True

            if arquivo_existe:
                break

            print("O arquivo com esse nome não existe!")
            continue
        return arquivo_selecionado

    def atualizar_status_arquivos(self):
        for arquivo in self.arquivos:
            arquivo.estado(self.commits.arquivos_commitados)

    def status(self):
        pass
        pass
        pass
        pass
        pass

