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
            while True:
                nome = input("Digite o nome do aluno: ")
                matricula = input("Digite a matrícula: ")
                aluno = Aluno(nome, matricula)
                print (pos_cadastro)
                opcao2 = int(input("Seleciona uma opção: "))
                match opcao2:
                    case 1:
                        entrada = input("Digite uma nota(Digite sair para sair): ")
                        if entrada.lower() == 'sair':
                            break 
                        try:
                            nota = float(entrada)
                            aluno.adicionar_nota(nota)
                        except ValueError:
                            print("❌ Por favor, digite um número válido ou 'sair'")
                    case 2:
                        print ('Voltando pro Cadastro de Alunos...')
                        break
        case 2:
            if aluno.notas:
                print(f"\n📊 ESTATÍSTICAS:")
                print(f"🔢 Total de notas: {len(aluno.notas)}")
                print(f"📊 Maior nota: {max(aluno.notas)}")
                print(f"📉 Menor nota: {min(aluno.notas)}")
                print(f"Media do aluno: {(aluno.media)}")
            print ('Saindo do sistema...')
            break

print (f'Nome do aluno: {aluno.nome}')
print (f'Matricula do aluno {aluno.matricula}')
print (f'Nota(s) do aluno: {aluno.notas}')
print (f'Media do aluno: {aluno.media}') 
        
