from Aluno import * 

menu_inicial = ''' 
    >>Cadastro de Alunos<<<
    1. Cadastrar Aluno(a)
    2. Sair do sistema
'''
pos_cadastro = '''
    Deseja adicionar uma nota a este aluno? 
    1. Adicionar nota(s)
    2. Sair 
'''
while True:
    print (menu_inicial)
    opcao = int(input("Seleciona uma opção: "))
    match opcao:
        case 1:
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula: ")
            aluno = Aluno(nome, matricula)
            
            # Pergunta quantas notas deseja adicionar
            while True:
                try:
                    qtd_notas = int(input("\n Quantas notas deseja adicionar? "))
                    if qtd_notas > 0:
                        break
                    else:
                        print("❌ Digite um número maior que 0")
                except ValueError:
                    print("❌ Digite um número válido")
            
            # Adiciona as notas uma por uma
            print(f"\n Digite as {qtd_notas} nota(s):")
            for i in range(qtd_notas):
                while True:
                    try:
                        nota = float(input(f"Nota {i+1}: "))
                        if aluno.adicionar_nota(nota):
                            break  # Sai do loop se a nota for válida
                    except ValueError:
                        print("❌ Digite um número válido")
            
            print(f"\n Todas as {qtd_notas} nota(s) foram adicionadas!")
            print(f" Média atual: {aluno.media:.1f}")
            print(f" Situação: {aluno.situacao()}")
        
        case 2:
            if 'aluno' in locals() and aluno.notas:
                print(f"\n ESTATÍSTICAS FINAIS:")
                print(f"Nome do aluno: {(aluno.nome)}")
                print(f" Total de notas: {len(aluno.notas)}")
                print(f" Maior nota: {max(aluno.notas)}")
                print(f" Menor nota: {min(aluno.notas)}")
                print(f" Média do aluno: {aluno.media:.1f}")
                print(f" Situação do aluno: {aluno.situacao()}")
            print('Saindo do sistema...')
            break
            #Odiei essa questao.

        
