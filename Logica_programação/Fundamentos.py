# %% [markdown]
# ## 1. Lógica de Programação

# %% [markdown]
# Tradução para Python:

# %%
# Traduzindo o pseudocódigo para Python
nota1 = 7.5
nota2 = 8.0

media = (nota1 + nota2) / 2

print(f"A média do aluno é: {media}")

if media >= 7.0:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado.")

# %% [markdown]
# ## 2. Variáveis: Declaração, Atribuição e Regras de Nomenclatura
# 
# Uma variável é um espaço na memória do computador destinado a armazenar dados. Em Python, a declaração e a atribuição de um valor a uma variável são feitas simultaneamente. Regras de Nomenclatura:
# 
# - Nomes de variáveis devem começar com uma letra ou um underscore (_).
# 
# - Não podem começar com um número.
# 
# - Podem conter apenas caracteres alfanuméricos e underscores (A-z, 0-9 e _).
# 
# - São "case-sensitive" (idade é diferente de Idade).

# %%
# Declaração e atribuição de variáveis
nome_completo = "Bob da Silva"   # String (texto)
idade = 30                       # Integer (inteiro)
altura = 1.76                    # Float (ponto flutuante)
eh_estudante = True              # Boolean (booleano)

# %%
print(f"Nome: {nome_completo}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura}m")
print(f"É estudante? {eh_estudante}")

# %%
# Exemplo de nomes de variáveis inválidos (descomente para ver o erro)
# 1nome = "Inválido"
# nome-completo = "Inválido"

# %% [markdown]
# Python é uma linguagem dinamicamente "tipada". Você não precisa declarar o tipo das variáveis ao criá-las, pois Python descobre automaticamente pelo valor atribuído:

# %%
x = 10        # tipo int
y1 = 10       # tipo int
y2 = "10"     # tipo str

# %%
type(x)

# %%
type(y1)

# %%
type(y2)

# %%
# Podemos somar tipos numéricos
print(x + y1)

# %%
# Mas não podemos somar número com string
# print(x + y2)

# %% [markdown]
# Ou seja, Python não "mistura" tipos incompatíveis automaticamente e isso mostra que a linguagem não é fracamente tipada.

# %% [markdown]
# ## 3. Escopo de Variáveis
# 
# O escopo de uma variável define onde ela pode ser acessada no código.
# 
# - Variáveis Globais: Declaradas fora de qualquer função. Podem ser acessadas de qualquer lugar do código.
# 
# - Variáveis Locais: Declaradas dentro de uma função. Só podem ser acessadas dentro daquela função.

# %%
# Variável Global
saudacao = "Olá, mundo!"
nome = "Aluno DSA"

# Função
def minha_funcao_dsa():
    
    # Variável Local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")

minha_funcao_dsa()

print(f"\nFora da função: {saudacao}")
print(f"\nFora da função: {nome}")

# %%
# Função
def minha_funcao_dsa():
    
    # Variável Local
    nome_local = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"\nAcessando a variável global de dentro da função: {saudacao}")

minha_funcao_dsa()

# Tentar acessar a variável local fora da função resultará em um erro (descomente para ver)
# print(f"Tentando acessar 'nome' fora da função: {nome_local}")

# %% [markdown]
# ## 4. Tipos de Dados Primitivos
# 
# Estes são os tipos de dados mais básicos em Python.

# %%
# Integer (Inteiro)
numero_inteiro = 100
print(f"Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# %%
# Float (Ponto Flutuante)
numero_decimal = 19.99
print(f"Valor: {numero_decimal}, Tipo: {type(numero_decimal)}")

# %%
# String (Texto)
texto = "Python é incrível!"
print(f"Valor: '{texto}', Tipo: {type(texto)}")

# %%
# Boolean (Booleano)
verdadeiro = True
falso = False
print(f"Valor: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"Valor: {falso}, Tipo: {type(falso)}")

# %% [markdown]
# ## 5. Operadores Aritméticos, de Comparação e Lógicos
# 
# ### 5.1. Operadores Aritméticos
# 
# Usados para realizar operações matemáticas.

# %%
# Definição de variáveis
a = 10
b = 3

# %%
# Usando operadores aritméticos
soma = a + b              # Adição
subtracao = a - b         # Subtração
multiplicacao = a * b     # Multiplicação
divisao = a / b           # Divisão (resultado é sempre float)
divisao_inteira = a // b  # Divisão inteira (descarta a parte decimal)
modulo = a % b            # Módulo (resto da divisão)
potencia = a ** b         # Potenciação

# %%
print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.2f}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {modulo}")
print(f"{a} ** {b} = {potencia}")

# %%
# As regras da matemática de aplicam aqui normalmente

# Variáveis
a = 10
b = 0

# Tentativa de divisão por zero
# a/b

# %%
# Cuidado. Isso não pode!
# 8 + 's'

# %%
# Mas isso pode! (não é soma, é concatenação)
'8' + 's' 

# %% [markdown]
# ### 5.2. Operadores de Comparação
# 
# Usados para comparar valores. O resultado é sempre um Boolean (True ou False).

# %%
# Definição de variáveis
x = 5
y = 10

# %%
# Operador "maior que"
x > y

# %%
# Operador "menor que"
x < y

# %%
# Operador "igual a"
x == y

# %%
# Operador "diferente de"
x != y

# %%
# Operador "maior ou igual a"
x >= 5

# %%
# Operador "menor ou igual a"
x <= y

# %%
print(f"{x} > {y} ? {x > y}")      # Maior que
print(f"{x} < {y} ? {x < y}")      # Menor que
print(f"{x} == {y} ? {x == y}")    # Igual a
print(f"{x} != {y} ? {x != y}")    # Diferente de
print(f"{x} >= 5 ? {x >= 5}")      # Maior ou igual a
print(f"{x} <= {y} ? {x <= y}")    # Menor ou igual a

# %% [markdown]
# ### 5.3. Operadores Lógicos
# 
# Usados para combinar expressões booleanas.

# %%
# Definição de variáveis
tem_dinheiro = True
tem_tempo = False

# %%
# Operador AND (e): Ambos precisam ser verdadeiros
print(f"O cliente pode viajar? {tem_dinheiro and tem_tempo}")

# %%
# Operador OR (ou): Pelo menos um precisa ser verdadeiro
print(f"O cliente pode viajar? {tem_dinheiro or tem_tempo}")

# %%
# Operador NOT (não): Inverte o valor booleano
print(f"O cliente pode viajar? {tem_dinheiro and not tem_tempo}")

# %% [markdown]
# ## 6. Manipulação de Strings
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Strings são sequências de caracteres e possuem muitos métodos úteis.

# %%
# Define uma variável do tipo string
frase = "  Aprender Python é muito divertido!  "

# %%
# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

# %%
# Tamanho da string
print(f"Tamanho da frase: {len(frase)}")

# %%
# Maiúsculas e Minúsculas
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")

# %%
# Remover espaços em branco do início e do fim
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# %%
# Substituir texto
print(f"Substituindo 'divertido' por 'legal': {frase_sem_espacos.replace('divertido', 'legal')}")

# %%
print(f"Frase sem espaços: '{frase_sem_espacos}'")

# %%
# Fatiamento (Slicing) - Acessando partes de uma string
# O índice em Python começa em 0
print(frase_sem_espacos)
print(f"O primeiro caractere: {frase_sem_espacos[0]}")
print(f"A palavra 'Python': {frase_sem_espacos[9:15]}") # Do índice 9 ao 14

# %% [markdown]
# ## 7. Estruturas de Dados - Listas
# 
# Listas são coleções ordenadas e **mutáveis** de itens. Podem conter diferentes tipos de dados.

# %%
# Criando uma lista
frutas = ["maçã", "banana", "laranja", "abacaxi"]
print(f"Lista de frutas: {frutas}")

# %%
type(frutas)

# %%
# Acessando um item pelo índice
print(f"A primeira fruta é: {frutas[0]}")
print(f"A última fruta é: {frutas[-1]}")

# %%
# Adicionando um item ao final da lista
frutas.append("uva")
print(f"Lista após adicionar 'uva': {frutas}")

# %%
# Removendo um item
frutas.remove("laranja")
print(f"Lista após remover 'laranja': {frutas}")

# %%
# Modificando um item
frutas[0] = "morango"
print(f"Lista após modificar o primeiro item: {frutas}")

# %%
# Podemos imprimir diretamente
print(frutas)

# %%
# Verificando o tamanho da lista
print(f"A lista tem {len(frutas)} frutas.")

# %%
# Deletando a lista
del frutas

# %%
# Lista não pode mais ser acessada
# print(frutas)

# %% [markdown]
# ## 8. Estruturas de Dados - Tuplas
# 
# Tuplas são coleções ordenadas e imutáveis de itens. Uma vez criadas, não podem ser alteradas.

# %%
# Criando uma tupla
coordenadas = (10.0, 20.5)
print(f"Tupla de coordenadas: {coordenadas}")

# %%
type(coordenadas)

# %%
# Acessando um item pelo índice
print(f"Coordenada X: {coordenadas[0]}")
print(f"Coordenada Y: {coordenadas[1]}")

# %%
# Tentativa de modificar uma tupla resultará em erro (descomente para ver)
# coordenadas[0] = 15.0

# %%
# Tuplas são úteis para dados que não devem ser alterados, como meses do ano, coordenadas, etc.
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"O primeiro dia da semana é: {dias_da_semana[0]}")

# %% [markdown]
# ## 9. Estruturas de Dados - Dicionários
# 
# Dicionários são coleções de pares chave: valor. São mutáveis.

# %%
# Criando um dicionário de informações de um aluno
aluno = {
    "nome": "Bob",
    "idade": 22,
    "curso": "Data Science Para Análise Multivariada",
    "aluno_ativo": True
}

# %%
print(f"Dicionário do aluno: {aluno}")

# %%
type(aluno)

# %%
# Acessando um valor pela sua chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}") # .get() é uma forma segura de acessar chaves

# %%
# Adicionando um novo par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário atualizado:\n {aluno}")

# %%
# Modificando um valor existente
aluno["idade"] = 23
print(f"Idade atualizada: {aluno['idade']}")

# %%
# Removendo um par chave-valor
del aluno["aluno_ativo"]
print(f"Dicionário após remover a chave 'ativo':\n {aluno}")

# %% [markdown]
# ## 10. Estruturas de Dados - Conjuntos (Sets)
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Conjuntos são coleções não ordenadas de itens únicos e mutáveis. Eles são úteis para remover duplicatas e realizar operações matemáticas de conjuntos (união, interseção).

# %%
# Criando um conjunto (note que os itens duplicados são removidos)
numeros = {1, 2, 3, 4, 2, 3, 5}
print(f"Conjunto de números (sem duplicatas): {numeros}")

# %%
type(numeros)

# %%
# Adicionando um item
numeros.add(6)
print(f"Após adicionar o valor 6: {numeros}")

# %%
# Removendo um item
numeros.remove(2)
print(f"Após remover o 2: {numeros}")

# %%
# Operações de conjunto
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# %%
# União (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(f"União de A e B: {uniao}")

# %%
# Interseção (elementos que estão em ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção de A e B: {intersecao}")

# %% [markdown]
# ## 11. Conversão Entre Tipos de Dados (Type Casting)
# 
# É a conversão de um tipo de dado para outro.

# %%
# Convertendo de string para número integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f"String '{numero_em_texto}' para Inteiro: {numero_inteiro}, Tipo: {type(numero_inteiro)}")

# %%
# Isso aqui não pode ser feito
# teste = "Esta é uma string de teste"
# teste_int = int(teste)
# print(teste_int)

# %%
# Convertendo de string para número float
numero_decimal_em_texto = "45.67"
numero_float = float(numero_decimal_em_texto)
print(f"String '{numero_decimal_em_texto}' para Float: {numero_float}, Tipo: {type(numero_float)}")

# %%
# Convertendo de número para string
idade = 25
idade_texto = str(idade)
print(f"Inteiro {idade} para String: '{idade_texto}', Tipo: {type(idade_texto)}")

# %%
# Convertendo entre estruturas de dados
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)

# %%
print(f"\nLista original: {lista_com_duplicatas}")
print(f"\nConvertida para Conjunto (remove duplicatas): {conjunto_unico}")
print(f"\nConvertida de volta para Lista: {lista_sem_duplicatas}\n")

# %% [markdown]
# ## 12. Entrada e Saída Padrão
# 
# A forma mais comum de interagir com o usuário é através da entrada (input) de dados pelo teclado e da saída (output) de informações na tela.
# 
# ### 12.1. Saída de Dados com print()
# 
# Já usamos bastante, mas aqui estão alguns recursos adicionais, como as f-strings.

# %%
# Variáveis
nome = "Juliana"
idade = 28
cidade = "Rio de Janeiro"

# Usando f-string (a forma mais moderna e recomendada)
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro no {cidade}.")

# Formatando números
preco = 49.95678
print(f"O preço do produto é R$ {preco:.2f}") # Formata para 2 casas decimais

# %% [markdown]
# ### 12.2. Entrada de Dados com input()
# 
# A função input() sempre retorna uma string. Por isso, é comum precisar fazer o type casting.

# %%
# Pedindo o nome do usuário (string)
nome_usuario = input("Qual é o seu nome? ")

# Pedindo a idade do usuário (precisa converter para int)
idade_usuario_str = input("Qual é a sua idade? ")
idade_usuario_int = int(idade_usuario_str)

from datetime import date

# Pega o ano corrente na data definida no sistema operacional da sua máquina
ano_atual = date.today().year 

# Processando os dados
ano_nascimento = ano_atual - idade_usuario_int

# Exibindo o resultado
print(f"\nOlá, {nome_usuario}! Bem-vindo(a).")
print(f"Você tem {idade_usuario_int} anos e nasceu aproximadamente em {ano_nascimento}.")


