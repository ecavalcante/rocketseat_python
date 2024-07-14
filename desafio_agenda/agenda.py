#Calcular e retornar espaços em branco de
#acordo com o tamanho da variavel <nome> para uma maximo de 50 caracteres
def inserir_espaco_branco(nome):
    espaco=''
    TAMANHO_CAMPO = 50;
    if len(nome) <= TAMANHO_CAMPO:
        espacos_completar = TAMANHO_CAMPO - len(nome)
        for indice in range(0,espacos_completar):
            espaco= espaco + " "
    return espaco

def adicionar_contato(contatos,nome,telefone,email):
   
    contatos.append({"nome":nome, "telefone":telefone, "email":email, "favorito":False})
    print("Contato adicionado com sucesso")
    
    return


def vizualisar_contatos(contatos):
    print("Contatos:")
    print("\n| Nome                                                   | Telefone                                          | E-mail                                            |")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = contato["favorito"]

        espaco_branco_nome = inserir_espaco_branco(nome)
        espaco_branco_telefone = inserir_espaco_branco(telefone)
        espaco_branco_email = inserir_espaco_branco(email)
        
        print(f"|⍟  {indice}. {nome}{espaco_branco_nome}| {telefone}{espaco_branco_telefone}| {email}{espaco_branco_email}|" if favorito else 
              f"|   {indice}. {nome}{espaco_branco_nome}| {telefone}{espaco_branco_telefone}| {email}{espaco_branco_email}|")
       # print("------------------------------------------------------------------------------")
    return

def editar_contato(contatos, indice, nome, telefone, email):
    indice_ajustado = int(indice) -1

    if len(nome) >0:
        contatos[indice_ajustado]["nome"] = nome
    if len(telefone) >0:
        contatos[indice_ajustado]["telefone"] = telefone
    if len(email) >0:
        contatos[indice_ajustado]["email"] = email

    print(f"Contato número {indice} alterado com sucesso.")
    return

def marcar_favorito(contatos, indice):
    indice_ajustado = int(indice) -1
    contatos[indice_ajustado]["favorito"] = True
    return


def exibir_favoritos(contatos):
    
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
                
            nome= contato["nome"]
            telefone= contato["telefone"]
            email= contato["email"]
            print(f"⍟ {indice}. {nome} - {telefone} - {email}")

    return

def remover_contato(contatos, indice):
    indice_ajustado = int(indice) -1
    nome = contatos[indice_ajustado]["nome"]
    pergunta = input(f"Deseja realmente remover o contato {indice}. {nome}? (s/n): ")

    if pergunta.lower() == 's':
        contatos.remove(contatos[indice_ajustado])
        print("\nContato removido!")
    
    return

contatos=[]

print("\n*******************************************************************************")
print("                               AGENDA DE CONTATOS                                ")
print("*******************************************************************************\n")


while True:
   

    print("     MENU    ")
    print("--------------------------------------")


    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Exibir favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    print("--------------------------------------\n")
    escolha = input("Imforme o item desejado: ")

    if escolha == '1':
        
        while True:
            print("Informe os dados do novo contato:")
            nome_contato = input("Nome: ")
            telefone_contato = input("telefone: ")
            email = input("E-mail: ")
            try:
                adicionar_contato(contatos, nome_contato, telefone_contato, email)
            except Exception as e:
                print(f"Erro interno, verifique os dados fornecidos - Erro:{e}")
            finally:       
                pergunta = input("Deseja adicionar outro contato? (s/n): ")
                if pergunta.lower() == 'n':
                    print("\nAdição de contatos finaliza!")
                    break
                    
                    
    elif escolha == '2':
        vizualisar_contatos(contatos)

    elif escolha == '3':
        
        if (len(contatos)>0):
            vizualisar_contatos(contatos)

            indice_escolha = input("\nInforme o índice do contato a ser alterado: ")
            print("Preencha os valores a serem alterados")

            resposta = input("Deseja alterar o nome? (s/n): ")
            nome_contato = input("Novo nome: ") if resposta.lower() =='s' else ''

            resposta ='n'
            resposta = input("Deseja alterar o telefone? (s/n): ")
            telefone_contato = input("Novo número de telefone: ") if resposta.lower() =='s' else ''

            resposta ='n'
            resposta = input("Deseja alterar o endereço de e-mail? (s/n): ")
            email = input("Novo endereço de e-mail: ") if resposta.lower() =='s' else ''

            try:
                editar_contato(contatos,indice_escolha,nome_contato,telefone_contato,email)
            except Exception as e:
                print(f"Algo deu errado contato não alterado. Erro {e}")
            else:
                vizualisar_contatos(contatos)
            finally:
                print("\nAlteração finalizada!")
        else:
            print("Sua lista de contatos está vazia")
    
    elif escolha =='4':
        if (len(contatos)>0):
            while True:
                vizualisar_contatos(contatos)
                indice = input("Informe o índice do contato a ser marcado como favorito: \n")
                try:
                    marcar_favorito(contatos, indice)
                except Exception as e:
                    print(f"Algo deu erro, o contato não foi marcado como favorito. erro {e}")
                    break
                else:
                    resposta = input("Deseja adicionar outro contato? (s/n): ")
                    if resposta.lower() == 'n':
                        print("\nMarcação de favoritos finalizada.")
                        vizualisar_contatos(contatos)
                        break
        else:
            print("Sua lista de contatos está vazia")

    elif escolha == '5':
        print("\nLista de contatos favoritos:")
        if (len(contatos)>0):
            print("------------------------------------------------------------------------------------------")
            exibir_favoritos(contatos)
            print("------------------------------------------------------------------------------------------\n")
        else:
            print("Sua lista de contatos está vazia")

    elif escolha=='6':
        if (len(contatos)>0):
            vizualisar_contatos(contatos)
            indice = input("Informe o índice do contato a ser removido: \n")
            if len(indice)>0 :
                try:
                    remover_contato(contatos,indice)
                    vizualisar_contatos(contatos)
                except Exception as e:
                    print(f"Algo deu errado contato não alterado. Erro {e}")
        else:
            print("Sua lista de contatos está vazia")
    elif escolha=='7':
        break
    elif escolha=='0': #menu de teste para preencher a lista com contatos fake
        adicionar_contato(contatos, "João da Silva", "(11)7843-6737", "joaosilva@gmail.com")
        adicionar_contato(contatos, "Renato Andrade", "(11)7843-6737", "renato@gmail.com")
        adicionar_contato(contatos, "Cecília Maitê Lopes", "(11) 98520-1433", "cecilia.maite.lopes@bemarius.com.br")
        adicionar_contato(contatos, "Betina Bárbara Moura", "(51) 98108-0518", "betina.barbara.moura@buzatto.pro")
        adicionar_contato(contatos, "Aurora Mirella Baptista", "(24) 99820-8148", "aurora.mirella.baptista@marsans.com.br")
