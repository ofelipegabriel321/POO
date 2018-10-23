import copy


class StageArea:
    def __init__(self, repositorio, arquivos_sa=[]):
        self.repositorio = repositorio
        self.arquivos_sa = arquivos_sa

    def add(self, arquivo):
        if arquivo.estado != 'unmodified':
            self.arquivos_sa.append(copy.deepcopy(arquivo))
            arquivo.tracked = True
            print("Arquivo adicionado à Stage Area")
        else:
            print("Esse arquivo não irá para Stage Area porque ele não foi modificado!")

    def verificar_se_esta_na_sa(self, arquivo):
        for arquivo_sa in self.arquivos_sa:
            if arquivo_sa.nome == arquivo.nome:
                return True
        return False

    def reset(self, arquivo):
        na_sa = False
        for arquivo_sa in self.arquivos_sa:
            if arquivo_sa.nome == arquivo.nome:
                arquivo_a_remover = arquivo_sa
                na_sa = True
        if na_sa:
            self.arquivos_sa.remove(arquivo_a_remover)
            arquivo.tracked = False
            print("Arquivo Removido da Stage Area")
        else:
            print("O arquivo não se localiza na Stage Area")

    def commitar(self, n_commit, commits):
        numero_commit = n_commit.gerar_numero_commit()
        commits.adicionar_commit(numero_commit, self.arquivos_sa, self.repositorio)
        self.arquivos_sa = []


class NumeroCommit:
    def __init__(self, numero_commit=-1):
        self.numero_commit = numero_commit

    def gerar_numero_commit(self):
        self.numero_commit += 1
        return self.numero_commit

