agenda = { 100: 'rodrigo' , 101: 'rita' }
numero = 102
print("-------------------")
print("Agenda de contatos")
print("-------------------")
print("1 - Cadastrar Contato \n2 - Atualizar Contato \n3 - Buscar Contato \n4 - Deletar Contato \n5 - Exibir lista de Contatos \n6 - Fechar Agenda de Contatos")

while True:
    print("--------------------------")
    opc = str(input("O que você deseja? "))
    print("--------------------------")
    if opc == '1':
        numero += 1
        nome = str(input("Digite o seu nome: "))
        agenda[numero] = nome

    elif opc == '2':
        num = int(input("Digite o contato: "))
        nome = str(input("Digite o novo nome: "))
        agenda[num] = nome

    elif opc == '3':
        usuario = str(input("Digite o nome do usuário: "))
        if usuario in agenda.values():
            print("Usuário encontrado!")
            for contato,nome in agenda.items():
                if nome == usuario:
                    print(f"Número: {contato} | Nome: {nome}")
            
        else:
            opc = str(input("1 - Sim \n2 - Não \nDeseja cadastrar novo Usuáro? "))
            print("-------------------------")
            if opc == "1":    
                while True:
                    numero = int(input("Digite o contato do Usuário: "))
                    if numero in agenda.keys():
                        print("Número já existe, Tente um novo!")
                    else:
                        agenda[numero] = usuario
                        break
            elif opc == "2":
                print("-------------------------")
                print("USUÁRIO NÃO ENCONTRADO!")
                print("-------------------------")
            else:
                print("-------------------------")
                print("   COMANDO INVÁLIDO!")
                print("-------------------------")
    
    elif opc == '4':
        print("--------------------------")
        print("  AGENDA DE CONTATOS")
        print("--------------------------")
        for contato,nome in agenda.items():
            print(f"Número: {contato} | Nome: {nome}")

        print("--------------------------")
        print("DIGITE O CONTATO QUE DESEJA \n     EXCLUIR DA AGENDA")
        print("-------------------------")
        opc = int(input("Contato: "))
        
        del agenda[opc]
        print("-------------------------")
        print("   CONTATO DELETADO!")
        print("-------------------------")
        print("   AGENDA ATUALIZADA")
        print("-------------------------")
        for contato,nome in agenda.items():
            print(f"Número: {contato} | Nome: {nome}")
        print("-------------------------")

    elif opc == '5':
        print("-------------------------")
        print("   AGENDA DE CONTATOS")
        print("-------------------------")
        for contato,nome in agenda.items():
            print(f"Número: {contato} | Nome: {nome}")
        
    elif opc == '6':
        print("Programa Encerrado com sucesso!")
        break
        
    else:
        print("Valor inválido, tente novamente")
