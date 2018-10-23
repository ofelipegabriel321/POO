from arquivo import *


class EditorDeTexto:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def exibir_texto_e_linhas(self):
        conteudo = self.arquivo.conteudo
        for indice, linha in enumerate(conteudo):
            print(indice, linha)

    def adicionar_texto(self):
        print("\nTexto e índices das linhas:")
        self.exibir_texto_e_linhas()

        indice_texto_adicionado = int(input("Digite o índice da linha em que deseja adicionar o texto(o texto dessa linha e das posteriores serão levados para baixo): "))

        print("Digite o conteúdo do texto (terminando com uma linha apenas com um S):")
        conteudo = []
        while True:
            linha = input()
            if linha == "S":
                break
            conteudo.append(linha)

        conteudo_arquivo = self.arquivo.conteudo

        self.arquivo.conteudo = []
        for indice_linha in range(len(conteudo_arquivo)):
            if indice_linha == indice_texto_adicionado:
                self.arquivo.conteudo.extend(conteudo)
            self.arquivo.conteudo.append(conteudo_arquivo[indice_linha])

    def remover_texto(self):
        print("\nTexto e índices das linhas:")
        self.exibir_texto_e_linhas()

        conteudo_arquivo = self.arquivo.conteudo

        indices_a_remover = list(map(int, input("Digite os índices (separados por espaço): ").split()))
        self.arquivo.conteudo = []
        for indice in range(len(conteudo_arquivo)):
            if not indice in indices_a_remover:
                self.arquivo.conteudo.append(conteudo_arquivo[indice])
