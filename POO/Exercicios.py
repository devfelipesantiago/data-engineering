# %% [markdown]
# #### Exercício 1
# 
# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

# %% [markdown]
# FUNÇÃO classifica_triangulo(lado1, lado2, lado3):
# 
#     SE lado1 == lado2 E lado2 == lado3 ENTÃO:
#   
#         RETORNE "Triângulo Equilátero"
#     
#     SENÃO SE lado1 == lado2 OU lado1 == lado3 OU lado2 == lado3 ENTÃO:
#   
#         RETORNE "Triângulo Isósceles"
#     
#     SENÃO:
#   
#         RETORNE "Triângulo Escaleno"
#     
# FIM FUNÇÃO

# %%
# Solução
def dsa_classifica_triangulo(lado1, lado2, lado3):
    
    """
    Classifica um triângulo com base nos comprimentos de seus lados.
    """
    
    # 1. Verifica se todos os lados são iguais
    if lado1 == lado2 == lado3:
        return "Triângulo Equilátero"
    
    # 2. Se não forem todos iguais, verifica se pelo menos dois são iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triângulo Isósceles"
        
    # 3. Se nenhuma das condições acima for verdade, os lados são todos diferentes
    else:
        return "Triângulo Escaleno"

# Testando a função
print(f"Lados 5, 5, 5: {dsa_classifica_triangulo(5, 5, 5)}")
print(f"Lados 5, 6, 5: {dsa_classifica_triangulo(5, 6, 5)}")
print(f"Lados 5, 6, 7: {dsa_classifica_triangulo(5, 6, 7)}")

# %% [markdown]
# #### Exercício 2
# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

# %% [markdown]
# FUNÇÃO exibe_tabuada(numero):
#   
#     IMPRIMA "Tabuada do " + numero
#   
#     PARA i DE 1 ATÉ 10 FAÇA:
#     
#         resultado = numero * i
#     
#         IMPRIMA numero + " x " + i + " = " + resultado
#   
#     FIM PARA
# 
# FIM FUNÇÃO

# %%
# Solução
def dsa_exibe_tabuada(numero):
    
    """
    Exibe a tabuada de multiplicação de um número.
    """
    
    print(f"--- Tabuada do {numero} ---")
    
    for i in range(1, 11): # O range vai de 1 até 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Testando a função
dsa_exibe_tabuada(7)

# %% [markdown]
# #### Exercício 3 
# 
# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

# %% [markdown]
# FUNÇÃO alunos_acima_da_media(turma):
# 
#     SE a turma estiver vazia ENTÃO:
#   
#         RETORNE "Dicionário de turma vazio."
# 
#     soma_notas = SOMA de todos os valores no dicionário turma
# 
#     media = soma_notas / NÚMERO de itens na turma
# 
#     CRIE uma lista vazia chamada "aprovados"
# 
#     PARA cada aluno, nota EM turma FAÇA:
# 
#         SE nota > media ENTÃO:
# 
#           ADICIONE aluno à lista "aprovados"
# 
#         FIM SE
# 
#       FIM PARA
# 
#     RETORNE a lista "aprovados"
# 
# FIM FUNÇÃO

# %%
# Solução
def dsa_alunos_acima_da_media(turma):
    
    """
    Calcula a média da turma e retorna os alunos com nota superior à média.
    """
    
    if not turma:
        return "Dicionário de turma vazio."

    # Calcula a soma de todas as notas
    soma_notas = sum(turma.values())
    
    # Calcula a média
    media = soma_notas / len(turma)

    print(f"A média da turma é: {media:.2f}")

    # Itera sobre o dicionário para encontrar alunos acima da média
    aprovados = []
    
    for aluno, nota in turma.items():
        if nota > media:
            aprovados.append(aluno)

    return aprovados

# Dados de exemplo
notas_turma = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.5, "Marcelo": 7.0, "Eliane": 5.5}

# Chama a função
print(f"Alunos acima da média: {dsa_alunos_acima_da_media(notas_turma)}")

# %% [markdown]
# #### Exercício 4
# 
# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

# %% [markdown]
# INÍCIO
# 
#     CRIE uma lista de números chamada "numeros"
#   
#     CRIE uma nova lista "quadrado_dos_pares" da seguinte forma:
#   
#         PARA cada x EM "numeros":
#     
#             SE x é par (x % 2 == 0):
#       
#                 INCLUA x ao quadrado (x ** 2) na nova lista
#         
#     IMPRIMA "quadrado_dos_pares"
#   
# FIM

# %%
# Solução

# Lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension com uma condição if
quadrado_dos_pares = [x ** 2 for x in numeros if x % 2 == 0]

print(f"Lista original: {numeros}")
print(f"Quadrado dos números pares: {quadrado_dos_pares}")

# %% [markdown]
# #### Exercício 5
# 
# Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.

# %% [markdown]
# FUNÇÃO calcula_imc(peso, altura):
# 
#     SE altura <= 0 ENTÃO:
#   
#         RETORNE "Altura inválida."
# 
#     imc = peso / (altura * altura)
#   
#     RETORNE imc
#   
# FIM FUNÇÃO

# %%
# Solução

# Função
def dsa_calcula_imc(peso, altura):
    
    """
    Calcula o Índice de Massa Corporal (IMC).

    Parâmetros:
    peso (float): peso em quilogramas.
    altura (float): altura em metros.

    Retorna:
    float: o valor do IMC calculado.
    """
    
    if altura <= 0:
        return "Altura inválida. Deve ser maior que zero."

    # Calcula o IMC
    imc = peso / (altura ** 2)
    
    return imc

# Testando a função com argumentos posicionais
meu_imc = dsa_calcula_imc(75, 1.80)
print(f"Seu IMC é: {meu_imc:.2f}")

# Testando com argumentos nomeados (keyword arguments)
outro_imc = dsa_calcula_imc(altura=1.65, peso=60)
print(f"O outro IMC é: {outro_imc:.2f}")

# %% [markdown]
# #### Exercício 6
# Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

# %% [markdown]
# INÍCIO
# 
#     CRIE uma lista de dicionários chamada "pessoas", onde cada dicionário tem 'nome' e 'idade'.
#   
#     CRIE uma nova lista "pessoas_ordenadas" ordenando a lista "pessoas".
#   
#     USE como critério de ordenação o valor da chave 'idade' de cada dicionário.
#   
#     IMPRIMA "pessoas_ordenadas"
#   
# FIM

# %%
# Solução

# Lista de dicionários
pessoas = [
    {'nome': 'Carla', 'idade': 32},
    {'nome': 'Bruno', 'idade': 25},
    {'nome': 'Ana', 'idade': 45},
    {'nome': 'Daniel', 'idade': 22}
]

# A função lambda extrai a idade de cada dicionário 'p' para ser usada como critério de ordenação
pessoas_ordenadas = sorted(pessoas, key = lambda p: p['idade'])

print("Lista original:")
print(pessoas)
print("\nLista ordenada por idade:")
print(pessoas_ordenadas)

# %% [markdown]
# #### Exercício 7
# 
# Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números são pares e quantos são ímpares.

# %% [markdown]
# FUNÇÃO conta_pares_impares(lista_numeros):
# 
#     CRIE um dicionário "contagem" com {'pares': 0, 'impares': 0}
# 
#     PARA cada numero EM lista_numeros FAÇA:
#   
#         SE numero é par ENTÃO:
#     
#             incremente contagem['pares'] em 1
#       
#         SENÃO:
#     
#           incremente contagem['impares'] em 1
#       
#         FIM SE
#     
#       FIM PARA
# 
#     RETORNE o dicionário "contagem"
#   
# FIM FUNÇÃO

# %%
# Solução

# Função
def dsa_conta_pares_impares(lista_numeros):
    
    """
    Conta a quantidade de números pares e ímpares em uma lista.
    """
    
    contagem = {'pares': 0, 'impares': 0}

    for numero in lista_numeros:
        if numero % 2 == 0:
            contagem['pares'] += 1
        else:
            contagem['impares'] += 1

    return contagem

# Lista de teste
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = dsa_conta_pares_impares(numeros)
print(f"Na lista, há {resultado['pares']} números pares e {resultado['impares']} números ímpares.")

# %% [markdown]
# #### Exercício 8
# 
# Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

# %% [markdown]
# FUNÇÃO filtra_emails_por_dominio(emails, dominio_desejado = "gmail.com"):
#   
#     CRIE uma nova lista da seguinte forma:
#     
#         PARA cada email EM emails:
#         
#           SE email termina com "@" + dominio_desejado:
#           
#             INCLUA o email na nova lista
#             
#       RETORNE a nova lista
# 
# FIM FUNÇÃO

# %%
# Solução

# Função
def dsa_filtra_emails_por_dominio(emails, dominio_desejado="gmail.com"):
    
    """
    Filtra uma lista de e-mails, retornando apenas aqueles de um domínio específico.
    """
    
    return [email for email in emails if email.endswith(f"@{dominio_desejado}")]

# Dados de exemplo
lista_emails = [
    "contato@gmail.com", 
    "vendas@yahoo.com", 
    "suporte@gmail.com", 
    "admin@outlook.com"
]

# Usando o domínio padrão ("gmail.com")
emails_gmail = dsa_filtra_emails_por_dominio(lista_emails)
print(f"E-mails do Gmail: {emails_gmail}")

# Especificando um domínio diferente
emails_yahoo = dsa_filtra_emails_por_dominio(lista_emails, dominio_desejado = "yahoo.com")
print(f"E-mails do Yahoo: {emails_yahoo}")

# %% [markdown]
# #### Exercício 9
# 
# Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

# %% [markdown]
# INÍCIO
#   
#     CRIE uma lista de frases.
#   
#     USE a função 'map' para aplicar uma transformação a cada frase na lista:
#     
#         A transformação deve:
#         
#             1. Converter a frase para MAIÚSCULAS.
# 
#             2. Anexar o texto " EM PYTHON" ao final.
# 
#     CONVERTA o resultado do 'map' para uma lista e armazene em "frases_modificadas".
#     
#     IMPRIMA cada item de "frases_modificadas".
# 
# FIM

# %%
# Solução

# Lista
frases = [
    "aprendendo a programar",
    "dominando estruturas de dados",
    "funções anônimas são poderosas"
]

# map() aplica a função lambda a cada item da lista 'frases'
# A lambda transforma a frase em maiúscula e concatena a string
frases_modificadas = list(map(lambda f: f.upper() + " EM PYTHON", frases))

for frase in frases_modificadas:
    print(frase)

# %% [markdown]
# #### Exercício 10
# 
# Crie um jogo onde o computador escolhe um número secreto entre 1 e 20. O jogador tem 5 tentativas para adivinhar. A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo. Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.

# %% [markdown]
# FUNÇÃO jogo_adivinhacao():
# 
#     numero_secreto = GERE um número aleatório entre 1 e 20
#     
#     tentativas = 5
# 
#     IMPRIMA mensagem de boas-vindas
# 
#     ENQUANTO tentativas > 0 FAÇA:
#     
#         IMPRIMA o número de tentativas restantes
#         
#         PEÇA ao jogador para digitar um palpite
#         
#         CONVERTA o palpite para um número inteiro
# 
#         SE palpite == numero_secreto ENTÃO:
#         
#             IMPRIMA "Parabéns! Você acertou!"
#             
#             INTERROMPA o loop
#             
#         SENÃO SE palpite < numero_secreto ENTÃO:
#         
#             IMPRIMA "Muito baixo!"
#             
#         SENÃO:
#         
#             IMPRIMA "Muito alto!"
#             
#         FIM SE
# 
#         DECREMENTE tentativas em 1
#         
#     FIM ENQUANTO
# 
#     SE o loop terminou sem que o jogador acertasse:
#     
#         IMPRIMA "Fim de jogo! O número era " + numero_secreto
# 
# FIM FUNÇÃO

# %%
# Solução

# Importa o pacote random para gerar números aleatórios
import random

# Define a função do jogo de adivinhação
def jogo_adivinhacao():
    
    # Gera um número secreto aleatório entre 1 e 20
    numero_secreto = random.randint(1, 20)

    # Define a quantidade de tentativas disponíveis
    tentativas = 5

    # Mensagem inicial para o jogador
    print("Adivinhe o número secreto entre 1 e 20. Você tem 5 tentativas!")

    # Loop que continua enquanto ainda houver tentativas
    while tentativas > 0:
        
        # Informa ao jogador quantas tentativas ainda restam
        print(f"\nVocê tem {tentativas} tentativa(s) restante(s).")
        
        # Solicita ao jogador um palpite (entrada de número inteiro)
        palpite = int(input("Digite seu palpite: "))

        # Verifica se o palpite é igual ao número secreto
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break  # Interrompe o loop caso o jogador acerte

        # Caso o palpite seja menor que o número secreto
        elif palpite < numero_secreto:
            print("Muito baixo!")

        # Caso o palpite seja maior que o número secreto
        else:
            print("Muito alto!")

        # Reduz o número de tentativas em 1
        tentativas -= 1

    # Este 'else' pertence ao 'while' e só será executado se o loop terminar sem 'break'
    else: 
        print(f"\nFim de jogo! O número secreto era {numero_secreto}.")

# Inicia o jogo chamando a função
jogo_adivinhacao()


