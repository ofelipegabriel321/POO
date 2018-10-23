class Arquivo:
    def __init__(self, nome, conteudo, estado='', tracked=False):
        self.nome = nome
        self.conteudo = conteudo
        self.estado = estado
        self.tracked = tracked

    def esta_commitado(self, arquivos_commitados):
        for arquivo_commitado in arquivos_commitados:
            if self.nome == arquivo_commitado.nome:
                return True
        return False

    def esta_nao_modificado(self, arquivos_commitados):
        for arquivo_commitado in arquivos_commitados:
            if self.nome == arquivo_commitado.nome and self.conteudo == arquivo_commitado.conteudo:
                return True
        return False

    def estado(self, arquivos_commitados): #esses sao os arquivos commitados
        if not self.tracked:
            self.estado = 'new file'
        if self.estado == 'deleted' and self.tracked:
            self.estado = 'deleted'  # com isso ele não é imprimido em listar arquivos
        elif self.esta_nao_modificado(arquivos_commitados):
            self.estado = 'unmodified' # com isso ele não aparece no git status, nem pode ser staged
        else:
            self.estado = 'modified'

    def remover_arquivo(self):
        self.estado = 'deleted'
