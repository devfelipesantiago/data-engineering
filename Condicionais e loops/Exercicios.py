# %% [markdown]
# #### Exercício 1
# 
# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

# %%
# Solução
def triangulo(a, b, c):
  if a == b and b == c:
    print('Triangulo Equilátero')
  elif a == b or b == c or a == c:
    print('Triangulo Isóceles')
  else:
    print('Triangulo Escaleno')

triangulo(2, 3, 4)
triangulo(2, 2, 2)
triangulo(2, 2, 4)


# %% [markdown]
# #### Exercício 2
# 
# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

# %%
# Solução
def tabuada(number):
  for i in range(1, 11):
    print(i * number)

tabuada(2)
tabuada(5)
tabuada(9)

# %% [markdown]
# #### Exercício 3 
# 
# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

# %%
# Solução
def media(notas):
  if not notas:
    return 'Dicionario vazio'
 

  quant_notas = len(notas.values())
  total = sum(notas.values())

  media_total = total / quant_notas
  aprovados = []

  for name, value in notas.items():
    if value > media_total:
      aprovados.append(name)

  print(f'A média das notas é {media_total:.2f}!\n')
  print(aprovados)

lista = {
  'Ana': 5.5,
  'Bruna': 10,
  'Amanda': 7,
  'José': 9,
  'João': 8,
  'Thiago': 6.5,
  'Dani': 7.7
}

media(lista)

# %% [markdown]
# #### Exercício 4
# 
# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

# %%
# Solução
new_list = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(new_list)

# %% [markdown]
# #### Exercício 5
# 
# Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.

# %%
# Solução
def cal_imc(peso, altura):
  if not peso or not altura:
    return 'Peso ou altura vazio'


  imc = peso / (altura*altura)
  return imc

print(cal_imc(100, 1.80))

# %% [markdown]
# #### Exercício 6
# 
# Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

# %%
# Solução

ordered_list = sorted(lista.items(), key=lambda p: p[0])

print(ordered_list)

# %% [markdown]
# #### Exercício 7
# 
# Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números são pares e quantos são ímpares.

# %%
# Solução
def contagem(lista_int):
  conta = {'pares': 0, 'impar': 0}

  for i in lista_int:
    if i % 2 == 0:
      conta['pares'] += i
    else:
      conta['impar'] += i

  return conta

numbers = range(1, 21)
print(contagem(numbers))

# %% [markdown]
# #### Exercício 8
# 
# Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

# %%
# Solução
def dominios(emails):
  dominio_desejado = '@gmail.com'
  return [email for email in emails if email.endswith(f'{dominio_desejado}')]

email_list = [
  'conta1@gmail.com',
  'conta2@hmail.com',
  'conta3@cmail.com',
  'conta4@gmail.com',
]

print(dominios(email_list))

# %% [markdown]
# #### Exercício 9
# 
# Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

# %%
# Solução
frases = [
  'asda asjdie kfjak',
  'asda asjdie kfjak',
  'asda asjdie kfjak'
]

frases_modificadas = list(map(lambda f: f.upper() + ' EM PYTHON', frases))

for frase in frases_modificadas:
  print(frase)


