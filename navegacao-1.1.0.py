# Breno Cagnato
# Tecnólogo em Gestão da tecnologia da informação

# Constantes para as opções do menu principal
gerenciar_estudantes = 1
gerenciar_professores = 2
gerenciar_disciplinas = 3
gerenciar_turmas = 4
gerenciar_matrículas = 5
sair = 9
estudantes = []

# Função para listar nomes
def listar_nomes():
    print('''
          ===== Listagem =====
          ''')
    if estudantes:
        for i, estudante in enumerate(estudantes, 1):
            nome_completo = estudante.get("nome_completo", "Nome não informado")
            codigo_estudante = estudante.get("codigo", "Codigo não informado")
            cpf = estudante.get("cpf", "cpf não informado")
            print(f'{i}. codigo: {codigo_estudante}, Nome: {nome_completo}, cpf: {cpf}')
    else:
        print('Não existem nomes cadastrados.')

    input('\nPressione ENTER para voltar...')

# Função para mostrar menu de operações
def mostrar_menu_operacoes(contexto):
    while True:
        print(f'''
        **** [{contexto}] MENU DE OPERAÇÕES ****
                [1] - Incluir.
                [2] - Listar.
                [3] - Atualizar.
                [4] - Excluir.
                [0] - Voltar ao menu principal.
            ''')
        opcao_operacao = int(input('Informe a opção desejada:'))
        
        # Apresenta a escolha do usuário
        operacoes = {
            1: 'Incluir',
            2: 'Listar',
            3: 'Atualizar',
            4: 'Excluir',
            0: 'Voltar ao menu principal'
        }

        if opcao_operacao in operacoes:
            escolha = operacoes[opcao_operacao]
            print(f'Você escolheu: {escolha}')

            # Algoritmo para inclusão de estudante
        if escolha == 'Incluir':
                    nome = input('Digite o nome (ou digite "sair" para sair): ')
                    if nome == "sair":
                        break
                    sobrenome = (input('Digite o sobrenome do estudante:'))
                    # Concatenar nome e sobrenome
                    nome_completo = f'{nome} {sobrenome}'
                    codigo_estudante = int(input('Digite o código do estudante:'))
                    cpf = input('Digite o CPF do estudante:')

                    # Adicionando o dicionário com as informações dos estudantes na lista
                    estudantes.append({'codigo': codigo_estudante,'nome_completo': nome_completo, 'cpf': cpf})

            # Algoritmo para listar nomes
        elif escolha == 'Listar':
            listar_nomes()

        elif escolha == 'Atualizar':
            # Lógica de atualização aqui
            pass

        # Verifica se o usuário escolheu voltar ao menu principal
        if opcao_operacao == 0:
            print('Você escolheu voltar ao menu principal...')
            break
        else:
            # Mensagem para opção inválida
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Loop principal para o menu principal
while True:
    print('''
                         ----------------
            <============ MENU PRINCIPAL ============>
                         ----------------

                [1] - Gerenciar estudantes.
                [2] - Gerenciar professores.
                [3] - Gerenciar disciplinas.
                [4] - Gerenciar turmas.
                [5] - Gerenciar matrículas.
                [9] - Sair
            ''')
    opcao = int(input('Informe a opção desejada:'))

    if opcao == sair:
        print("Você pediu para sair.")
        print("Fim da aplicação.")
        break  # Encerra o loop e finaliza o programa
    elif opcao == gerenciar_estudantes:
        mostrar_menu_operacoes('Estudantes')
    elif opcao == gerenciar_professores:
        print("EM DESENVOLVIMENTO")
        input('\nPressione ENTER para voltar!')
    elif opcao == gerenciar_disciplinas:
        print("EM DESENVOLVIMENTO")
        input('\nPressione ENTER para voltar!')
    elif opcao == gerenciar_turmas:
        print("EM DESENVOLVIMENTO")
        input('\nPressione ENTER para voltar!')
    elif opcao == gerenciar_matrículas:
        print("EM DESENVOLVIMENTO")
        input('\nPressione ENTER para voltar!')
    else:
        print("Opção inválida. Por favor, tente novamente.")
