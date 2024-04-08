# Version 1.1.0

# Constantes para as opções do menu principal
gerenciar_estudantes = 1
gerenciar_professores = 2
gerenciar_disciplinas = 3
gerenciar_turmas = 4
gerenciar_matrículas = 5
sair = 9

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
        mostrar_menu_operacoes('Professores')
    elif opcao == gerenciar_disciplinas:
        mostrar_menu_operacoes('Disciplinas')
    elif opcao == gerenciar_turmas:
        mostrar_menu_operacoes('Turmas')
    elif opcao == gerenciar_matrículas:
        mostrar_menu_operacoes('Matrículas')
    else:
        print("Opção inválida. Por favor, tente novamente.")
