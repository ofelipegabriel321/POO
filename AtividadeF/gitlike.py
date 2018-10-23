from repositorios import Repositorios
from stagearea import StageArea, NumeroCommit
from editordetexto import EditorDeTexto

def main():
    menu_repositorios = "\n\033[0;33;m*----------+++ GIT LIKE +++----------*\n" \
                        "|1 - Criar Repositório(já com INIT)  |\n" \
                        "|2 - Listar Repositórios             |\n" \
                        "|3 - Acessar Repositório             |\n" \
                        "|0 - Sair                            |\n" \
                        "*------------------------------------*\n\033[1;;m" \
                        "Digite a opção: "

    menu_repositorio = "\n\033[0;33;m*------------+++ GIT LIKE +++------------*\n" \
                       "|1 - Criar Repositório                   |\n" \
                       "|2 - Listar Repositórios                 |\n" \
                       "|3 - Acessar outro Repositório           |\n" \
                       "|4 - Criar Arquivo                       |\n" \
                       "|5 - Listar Arquivos                     |\n" \
                       "|6 - Editar Arquivo                      |\n" \
                       "|7 - Adicionar à Stage Area(ADD)         |\n" \
                       "|8 - Remover da Stage Area(RESET)        |\n" \
                       "|9 - Commitar os arquivos da SA(COMMIT)  |\n" \
                       "|10 - Status                             |\n" \
                       "|11 - Log                                |\n" \
                       "*----------------------------------------*\n\033[1;;m" \
                       "Digite a opção: "

    menu_editor = "\n\033[0;34;m*--------+++ EDITOR DE TEXTO +++--------*\n" \
                  "|1 - Exibir linhas do texto enumeradas  |\n" \
                  "|2 - Adicionar Texto                    |\n" \
                  "|3 - Remover Texto                      |\n" \
                  "|0 - Fechar Editor                      |\n" \
                  "*---------------------------------------*\n\033[1;;m" \
                  "Digite a opção: "

    repositorios = Repositorios()
    numero_commit = NumeroCommit()

    ir_para_diretorio = False
    while True:
        opcao = int(input(menu_repositorios))
        if opcao == 0:
            print("\nFechando o Git Like...")
            break
        elif opcao == 1:
            repositorios.criar_repositorio()
        elif opcao == 2:
            repositorios.listar_repositorios()
        elif opcao == 3:
            repositorio = repositorios.acessar_repositorio()
            if repositorio:
                ir_para_repositorio= True
                break
        else:
            print("Opção inválida!")
        input("\n\033[1;36;mAperte ENTER para continuar...")

    if ir_para_repositorio:
        stagearea = StageArea(repositorio)
        while True:
            repositorio.atualizar_status_arquivos()
            opcao = int(input(menu_repositorio))
            if opcao == 0:
                print("\nFechando o Git Like...")
                break
            elif opcao == 1:
                repositorios.criar_repositorio()
            elif opcao == 2:
                repositorios.listar_repositorios()
            elif opcao == 3:
                repositorio = repositorios.acessar_repositorio()
            elif opcao == 4:
                repositorio.criar_arquivo()
            elif opcao == 5:
                repositorio.listar_arquivos()
            elif opcao == 6:
                arquivo_selecionado = repositorio.selecionar_arquivo()
                if arquivo_selecionado:
                    editor_de_texto = EditorDeTexto(arquivo_selecionado)
                    while True:
                        opcao = int(input(menu_editor))
                        if opcao == 0:
                            print("\nSaindo do editor...")
                            break
                        elif opcao == 1:
                            editor_de_texto.exibir_texto_e_linhas()
                        elif opcao == 2:
                            editor_de_texto.adicionar_texto()
                        elif opcao == 3:
                            editor_de_texto.remover_texto()
                        else:
                            print("Opção Inválida!")

                        input("\n\033[1;36;mAperte ENTER para continuar...")
            elif opcao == 7:
                arquivo_selecionado = repositorio.selecionar_arquivo()
                if arquivo_selecionado:
                    stagearea.add(arquivo_selecionado)
            elif opcao == 8:
                arquivo_selecionado = repositorio.selecionar_arquivo()
                if arquivo_selecionado:
                    stagearea.reset(arquivo_selecionado)

            elif opcao == 9:
                stagearea.commitar(numero_commit, repositorio.commits)
                print("Arquivos Commitados")

            elif opcao == 10:
                repositorio.status()

            elif opcao == 11:
                repositorio.commits.log()

            else:
                print("Opção inválida")

            input("\n\033[1;36;mAperte ENTER para continuar...")


if __name__ == '__main__':
    main()
