# %% [markdown]
# ## 1. Tomada de Decisão com Estruturas Condicionais

# %% [markdown]
# As estruturas condicionais (if, elif, else) permitem que o programa execute diferentes blocos de código com base em certas condições.

# %%
# Define a variável
nota = 8.5

# Agora checamos o valor da variável e tomamos decisões
if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado.")

# %%
# Define a variável
idade = 40

# Agora checamos o valor da variável e tomamos decisões
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# %% [markdown]
# ## 2. Estruturas de Repetição
# 
# As estruturas de repetição (for e while) são usadas para executar um bloco de código várias vezes.
# 
# ### Loop for
# 
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

# %%
# Define uma lista
frutas = ["maçã", "banana", "cereja"]

# Imprime a mensagem
print("Frutas disponíveis:")

# Loop pela lista
for fruta in frutas:
    print(f"- {fruta}")

# %%
# Criando uma tupla
cores = ("vermelho", "verde", "azul")

# Loop for percorrendo a tupla
for cor in cores:
    print(cor)

# %%
# Criando um dicionário com o número de cursos em Formações da DSA
formacoes_dsa = {"Formação Cientista de Dados": 6, "Formação Analista de Dados": 4, "Formação Engenheiro de Dados": 5}

# Loop for percorrendo chaves e valores
for chave, valor in formacoes_dsa.items():
    print(chave, ":", valor)

# %%
# Exemplo com a função range()
print("\nContagem até 5:")
for numero in range(6):  # Gera números de 0 a 5
    print(numero)

# %% [markdown]
# ### Loop while
# 
# O loop while executa um bloco de código enquanto uma condição for verdadeira.

# %%
# Define a variável
contador = 5

# Imprime a mensagem
print("Contagem regressiva:")

# Loop
while contador > 0:
    print(contador)
    contador -= 1

# %%
# Define a variável
contador = 0

# Imprime a mensagem
print("Contagem regressiva:")

# Loop
while contador > 1:
    print(contador)
    contador -= 1

# %%
# CUIDADO - LOOP INFINITO - PODE TRAVAR O JUPYTER OU MESMO SUA MÁQUINA
# Define a variável
#contador = 2

# Imprime a mensagem
#print("\nContagem regressiva:")

# Loop
#while contador > 1:
    #print(contador)
    #contador -= 1

# %% [markdown]
# O for em Python é usado quando você já sabe sobre o que quer iterar (como uma lista, tupla, dicionário, string, range, etc.). Ele percorre cada elemento de uma sequência ou iterável de forma automática, sem que você precise gerenciar manualmente a condição de parada.
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Já o while é usado quando você não sabe previamente quantas vezes o loop vai rodar e a repetição depende de uma condição booleana que deve continuar verdadeira para que o loop prossiga. Você precisa cuidar manualmente de alterar o estado dessa condição para evitar loops infinitos.
# 
# Em resumo:
# 
# - for → ideal quando você já tem uma coleção ou um número definido de repetições.
# 
# - while → ideal quando a repetição depende de uma condição que pode mudar dinamicamente ao longo da execução.

# %% [markdown]
# ## 3. Iteração Sobre Estruturas de Dados com Loops e Condicionais
# 
# Iterar significa percorrer os elementos de uma coleção de dados.

# %%
# Tupla de números
numeros = (3, 7, 10, 15, 20)

# Itera pela tupla e mostra apenas os números pares
for n in numeros:
    if n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f'{n} é impar')

# %%
# Lista de nomes
nomes = ["Ana", "Bruno", "Carlos", "Amanda", "Beatriz"]

# Itera pela lista e mostra apenas os nomes que começam com 'A'
for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome encontrado com A: {nome}")

# %%
# Dicionário com produtos e preços
produtos = {"arroz": 25, "feijão": 12, "carne": 45, "macarrão": 8}

# Itera pelo dicionário e mostra apenas produtos acima de 20 reais
for item, preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")

# %% [markdown]
# ## 4. Controle de Fluxo em Loops
# 
# As instruções break e continue alteram o fluxo de execução de um loop.
# 
# ### break
# 
# A instrução break para a execução do loop imediatamente.

# %%
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mensagem
print("\nBuscando pelo número 5...")

# Loop com break
for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado!")
        break  # Sai do loop
    print(f"Verificando {numero}...")

# %%
# Mensagem
print("\nImprimindo apenas os números ímpares:")

# Loop com instrução continue
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(numero)

# %% [markdown]
# ## 5. Comprehensions (List, Set, Dict e Generator) em Python
# 
# Estas estruturas são consideradas construtores sintáticos (syntactic constructs) ou, mais formalmente, expressões de compreensão (comprehension expressions).
# 
# Na documentação oficial Python, os nomes são:
# 
# - List comprehension → expressão que gera listas.
# 
# - Set comprehension → expressão que gera conjuntos.
# 
# - Dict comprehension → expressão que gera dicionários.
# 
# - Generator expression → expressão que gera iteradores (e pode ser convertido em tupla, lista, etc.).
# 
# Ou seja, o termo técnico mais amplo é comprehension: uma forma mais curta e expressiva de construir coleções (ou geradores) a partir de iteráveis com filtros e transformações aplicadas inline.

# %%
# Criando uma lista de quadrados dos números de 0 a 9
quadrados = [x ** 2 for x in range(10)]

# Print
print(f"\nQuadrados de 0 a 9: {quadrados}")

# %%
type(quadrados)

# %%
# Criando uma lista de números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]

# Print
print(f"Números pares de 0 a 20: {pares}")

# %%
type(pares)

# %%
# Cria um dicionário com números e seus quadrados
quadrados_dict = {x: x ** 2 for x in range(6)}
print(quadrados_dict)

# %%
type(quadrados_dict)

# %%
# Conjunto de quadrados (sem valores repetidos)
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4]}
print(quadrados_set)

# %%
type(quadrados_set)

# %%
# Generator expression (não é tupla ainda)
#gen = (x ** 2 for x in range(6))
#print(gen)

# Convertendo em tupla
quadrados_tuple = tuple(x ** 2 for x in range(6))
print(quadrados_tuple)

# %%
type(quadrados_tuple)

# %% [markdown]
# Um generator em Python é um iterador especial que não armazena todos os valores na memória de uma vez, mas sim gera cada valor sob demanda. No caso, gen não é uma lista de quadrados de 0 a 5, mas um objeto que sabe como calcular esses valores quando você pedir. A grande vantagem é que o generator economiza memória. 

# %% [markdown]
# ## 6. Trabalhando com Funções
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.

# %%
# Definindo uma função simples
def dsa_saudacao():
    """Esta função exibe uma saudação simples."""
    print("\nOlá! Bem-vindo ao Python.")

# %%
# Chamando a função
dsa_saudacao()

# %%
# Chamando a função mais uma vez
dsa_saudacao()

# %%
# Definindo uma função que retorna um valor
def dsa_soma_numeros(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

# %%
# Chamando a função e armazenando o resultado em uma variável
resultado = dsa_soma_numeros(433253.213, 3234367.45)

# Print
print(f"O resultado da soma é: {resultado}")

# %% [markdown]
# ## 7. Parâmetros e Argumentos de Funções
# 
# Diferentes formas de passar informações para as funções.

# %%
# Argumentos posicionais
def apresentacao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# %%
# Chamando a função
apresentacao("Ana", 25)

# %%
# Chamando a função - CUIDADO!!!
apresentacao(25, "Ana")

# %%
# Argumentos nomeados
apresentacao(idade = 30, nome = "Bob")

# %%
# Parâmetros com valores padrão (default)
def saudacao_completa(nome, saudacao = "Olá"):
    print(f"{saudacao}, {nome}!")

# %%
# Chamando a função
#saudacao_completa()

# %%
# Chamando a função
saudacao_completa("Maria")

# %%
# Chamando a função
saudacao_completa("Bob", "Bom dia")

# %% [markdown]
# ----

# %% [markdown]
# ### 7.1. Trabalhando com Número Variado de Argumentos em Funções Python
# 
# Em Python, *args e **kwargs são formas de tornar funções mais flexíveis, permitindo receber um número variável de argumentos sem precisar definí-los todos na assinatura da função.
# 
# *args – argumentos posicionais variáveis
# 
# O asterisco (*) antes do nome indica que a função pode receber qualquer quantidade de argumentos posicionais. Esses valores chegam dentro da função como uma tupla.
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# **kwargs – argumentos nomeados variáveis
# 
# Os dois asteriscos (**) indicam que a função pode receber qualquer quantidade de argumentos nomeados (chave e valor). Esses valores chegam dentro da função como um dicionário.

# %%
# Argumentos de tamanho variável (*args)
def soma_numeros(*args):
    """Soma um número variável de argumentos."""
    total = 0
    for numero in args:
        total += numero
    return total

# %%
print(f"Soma dos Números: {soma_numeros(13, 23, 33, 43, 53)}")

# %%
print(f"Soma dos Números: {soma_numeros(1, 2, 3)}")

# %%
print(f"Soma dos Números: {soma_numeros(10, 400, 0.3, 120)}")

# %%
# Argumentos de tamanho variável (**kwargs)
def exibe_info_pessoa(**kwargs):
    
    """Exibe informações passadas como pares chave-valor."""
    
    print("\nInformações da Pessoa:\n")
    
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")

# %%
# Chamando a função
exibe_info_pessoa(nome = "Carla", 
                      profissao = "Engenheira de Dados", 
                      hobby = "Leitura")

# %%
# Chamando a função
exibe_info_pessoa(nome = "Bob", profissao = "Cientista de Dados")

# %% [markdown]
# ## 8. Funções Anônimas (Expressão Lambda)
# 
# São pequenas funções anônimas definidas com a palavra-chave lambda.

# %%
# Uma função lambda que dobra um número
dobro = lambda x: x * 2

# Print
print(f"O dobro de 7 é: {dobro(7)}")

# %% [markdown]
# A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).
# 
# Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez, dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.
# 
# Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.

# %%
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lambda que retorna o quadrado de cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)  # [1, 4, 9, 16, 25]

# %% [markdown]
# Aqui:
# 
# - lambda x: x**2 define uma função anônima que calcula o quadrado.
# 
# - map() aplica essa função a cada elemento da lista.
# 
# - list() converte o resultado do map (um iterador) de volta para lista.
# 
# 👉 Também daria para fazer com list comprehension, mas aí não seria lambda.

# %%
# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Primeiro calculamos os quadrados com map + lambda
quadrados = list(map(lambda x: x ** 2, numeros))

# Agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

print("Quadrados:", quadrados)              # [1, 4, 9, 16, 25, 36]
print("Quadrados pares:", quadrados_pares)  # [4, 16, 36]

# %% [markdown]
# ## 9. Módulos da Biblioteca Padrão Python
# 
# Python vem com uma vasta biblioteca de módulos para todo tipo de tarefa. E se precisar de mais, visite o repositório oficial de pacotes da linguagem:
# 
# https://pypi.org

# %%
# Usando o módulo 'math' para funções matemáticas
import math

# %%
# Calcula a raiz quadrada
raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadrada}")

# %%
# Usando o módulo 'random' para gerar números aleatórios
import random

# %%
# Gera um inteiro entre 1 e 100
numero_aleatorio = random.randint(1, 100) 
print(f"Um número aleatório entre 1 e 100: {numero_aleatorio}")

# %%
# Seleciona aleatoriamente uma cidade da lista
cidade_aleatoria = random.choice(["Rio de Janeiro", "Salvador", "Curitiba"])
print(f"Cidade escolhida aleatoriamente: {cidade_aleatoria}")

# %% [markdown]
# ## 10. Criando e Importando Seus Próprios Módulos
# 
# Você pode organizar seu código em arquivos (módulos) e importá-los em outros scripts.
# 
# ### Passo 1: Crie o arquivo do módulo.

# %%
%%writefile modulo.py

def saudacao(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Tudo bem?"

PI = 3.14159

# %% [markdown]
# ### Passo 2: Crie o script principal para importar o módulo.

# %%
%%writefile principal.py

# Conteúdo do arquivo dsaprincipal.py

# Importa o módulo inteiro
import modulo

# Usa a função e a variável do módulo
mensagem = modulo.saudacao("Mundo")
print(mensagem)
print(f"O valor de PI do nosso módulo é: {modulo.PI}")

# Outra forma: importando itens específicos
from modulo import saudacao, PI

mensagem_direta = saudacao("Aluno DSA")
print(mensagem_direta)
print(f"Valor de PI importado diretamente: {PI}")

# %% [markdown]
# Para executar, você rodaria o arquivo principal.py. O Python automaticamente encontraria e usaria o conteúdo de meu_modulo.py.


