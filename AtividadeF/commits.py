import time


class Commits:
    def __init__(self, commits=[], arquivos_commitados=[]):
        self.commits = commits
        self.arquivos_commitados = arquivos_commitados

    def adicionar_commit(self, numero_commit, arquivos, repositorio):
        commit = input("Digite o commit: ")
        data = time.asctime(time.localtime())
        self.commits.append({'numero': numero_commit, 'comentario': commit, 'data': data})
        for arquivo in arquivos:
            commitado = False
            for arquivo_commitado in self.arquivos_commitados:
                if arquivo.nome == arquivo_commitado.nome:
                    commitado = True
                    self.arquivos_commitados.remove(arquivo_commitado)
                    self.arquivos_commitados.append(arquivo)
                    break

            if not commitado:
                self.arquivos_commitados.append(arquivo)

            for arquivo_repositorio in repositorio.arquivos:
                if arquivo.nome == arquivo_repositorio.nome:
                    arquivo_repositorio.tracked = True

    def log(self):
        for commit in self.commits[::-1]:
            print("\033[0;33;mcommit {}\033[m".format(commit['numero']))
            print("Data: {}".format(commit['data']))
            print("\n\t{}\n".format(commit['comentario']))
