# %% [markdown]
# #### Exercício 1
# 
# Escreva um programa que peça ao usuário para digitar seu nome e, em seguida, imprima uma mensagem de boas-vindas com o nome fornecido.

# %%
# Solução
user_name = input('Digite seu nome:')
print(f'Seja bem vindo {user_name}!')

# %% [markdown]
# #### Exercício 2
# 
# Crie duas variáveis, numero1 e numero2, e atribua a elas valores inteiros. Calcule a soma, subtração, multiplicação e divisão dessas variáveis e imprima os resultados.

# %%
# Solução
number1 = 91
number2 = 29

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 // number2)


# %% [markdown]
# #### Exercício 3 
# 
# Qual é a principal diferença entre uma variável de escopo local e uma de escopo global?

# %%
# Solução
# Escopo global voce pode acessar em qualquer parte do seu codigo, local somente dentro da função que foi criada a variável.

# %% [markdown]
# #### Exercício 4
# 
# Crie uma variável chamada saldo com o valor 500.50 (float). Em seguida, crie uma variável saque com o valor 200.25 (float). Subtraia o saque do saldo e imprima o saldo final formatado para duas casas decimais.

# %%
# Solução
saldo = 500.50
saque = 200.25
print(saldo - saque)

# %% [markdown]
# #### Exercício 5
# 
# Declare uma variável booleana chamada **tem_carteira_de_motorista** e atribua a ela o valor True. Imprima uma mensagem que diga "Pode dirigir" se a variável for verdadeira e "Não pode dirigir" caso contrário.

# %%
# Solução
tem_carteira_de_motorista = True
if tem_carteira_de_motorista:
  print('Pode dirigir')

# %% [markdown]
# #### Exercício 6
# 
# Crie duas variáveis: 
# 
# - idade_ana = 25
# - idade_beto = 30
# 
# Use operadores de comparação para verificar se a idade de Ana é menor que a de Beto e imprima o resultado booleano.

# %%
# Solução
idade_ana = 25
idade_beto = 30

print(idade_ana < idade_beto)

# %% [markdown]
# #### Exercício 7
# 
# Receba um número inteiro do usuário e use o operador de módulo (%) para verificar se o número é par ou ímpar. Imprima o resultado.
# 
# Obs: Não estudamos ainda os condicionais, mas pesquise se necessário e tente resolver.

# %%
# Solução
number = input('Digite um numero inteiro:')
if int(number) % 2 == 0:
  print(f'O numero {number} é Par')
else:
  print(f'O numero {number} é Impar')

# %% [markdown]
# #### Exercício 8
# 
# Crie duas variáveis booleanas: 
# 
# - chovendo = True
# - guarda_chuva = False
# 
# Use operadores lógicos para verificar se uma pessoa vai se molhar (se está chovendo E ela não tem guarda-chuva).

# %%
# Solução
chovendo = True
guarda_chuva = False
vai_se_molhar = chovendo and guarda_chuva
print(f'A pessoa vai se molhar? {vai_se_molhar}')

# %% [markdown]
# #### Exercício 9
# 
# Calcule a potência de 2 elevado a 10 e imprima o resultado.

# %%
# Solução
print(2**10)

# %% [markdown]
# #### Exercício 10
# 
# Converta a string "2026" para um tipo inteiro e armazene-a em uma variável chamada ano. Em seguida, some 1 a essa variável e imprima o novo ano.

# %%
# Solução
ano = int('2026')
print(1 + ano)

# %% [markdown]
# #### Exercício 11
# 
# Crie a string:
# 
# frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   ". 
# 
# Remova os espaços em branco do início e do fim da string e imprima a nova string.

# %%
# Solução
frase = ' Python é uma linguagem poderosa      '
print(frase.strip())

# %% [markdown]
# #### Exercício 12
# 
# Na string do exercício anterior (já sem os espaços), converta toda a frase para letras maiúsculas.

# %%
# Solução
print(frase.lower())

# %% [markdown]
# #### Exercício 13
# 
# Ainda usando a mesma string, substitua a palavra "poderosa" por "incrível".

# %%
# Solução
print(frase.replace('poderosa', 'incrivel'))

# %% [markdown]
# #### Exercício 14
# 
# Verifique e imprima o número total de caracteres na string frase (após as modificações dos exercícios anteriores).

# %%
# Solução
frase = 'Python é uma linguagem poderosa' 
print(len(frase))

# %% [markdown]
# #### Exercício 15
# 
# Use fatiamento (slicing) para extrair e imprimir apenas a palavra "Python" da string frase.

# %%
# Solução
print(frase[0:6])

# %% [markdown]
# #### Exercício 16
# 
# Crie uma lista chamada compras com os seguintes itens: "arroz", "feijão", "macarrão", "carne". Imprima a lista.

# %%
# Solução
itens = ["arroz", "feijão", "macarrão", "carne"]

# %% [markdown]
# #### Exercício 17
# 
# Adicione o item "leite" ao final da lista compras e imprima a lista atualizada.

# %%
# Solução
itens.append('leite')
print(itens)

# %% [markdown]
# #### Exercício 18
# 
# Acesse e imprima o segundo item da lista compras.

# %%
# Solução
print(itens[1])

# %% [markdown]
# #### Exercício 19
# 
# Remova o item "macarrão" da lista compras e imprima a lista final.

# %%
# Solução
itens.remove('macarrão')
print(itens)

# %% [markdown]
# #### Exercício 20
# 
# Crie uma lista de números de 1 a 5. Use uma função para calcular e imprimir o tamanho (número de elementos) dessa lista.

# %%
# Solução
numbers = [1,2,3,4,5]
print(len(numbers))

# %% [markdown]
# #### Exercício 21
# 
# Crie uma tupla chamada meses com os três primeiros meses do ano: "Janeiro", "Fevereiro", "Março".

# %%
# Solução
meses = ('Janeiro',
  'Fevereiro',
  'Março',
  'Abril'
)
print(meses)

# %% [markdown]
# #### Exercício 22
# 
# Tente adicionar o mês "Abril" à tupla meses. O que acontece? Explique o resultado.

# %%
# Solução
meses[5] = 'Maio'
print(meses)
#'tuple' object does not support item assignment

# %% [markdown]
# #### Exercício 23
# 
# Acesse e imprima o primeiro mês da tupla meses.

# %%
# Solução
print(meses[0])

# %% [markdown]
# #### Exercício 24
# 
# Crie um dicionário chamado filme com as seguintes chaves e valores: 
# 
# - titulo = "O Poderoso Chefão",
# - ano = 1972
# - diretor = "Francis Ford Coppola"

# %%
# Solução
filmes = {
  'titulo': 'O Poderoso Chefão',
  'ano': 1972,
  'diretor': 'Francis Ford Coppola' 
}
print(filmes)

# %% [markdown]
# #### Exercício 25
# 
# Acesse e imprima o ano de lançamento do filme a partir do dicionário.

# %%
# Solução
print(filmes['ano'])

# %% [markdown]
# #### Exercício 26
# 
# Adicione uma nova chave genero com o valor "Drama" ao dicionário filme e imprima o dicionário completo.

# %%
# Solução
filmes['genero'] = 'Drama'
print(filmes)

# %% [markdown]
# #### Exercício 27
# 
# Modifique o valor da chave ano para 1973 e imprima o dicionário atualizado.

# %%
# Solução
filmes['ano'] = 1973
print(filmes)

# %% [markdown]
# #### Exercício 28
# 
# Crie uma lista com os seguintes números: [1, 2, 2, 3, 4, 4, 5, 1]. Use um conjunto para remover os números duplicados e imprima o resultado.

# %%
# Solução
lista = [1,2,2,3,4,4,5,1]
print(set(lista))

# %% [markdown]
# #### Exercício 29
# 
# Crie dois conjuntos: 
# 
# - set_a = {1, 2, 3, 4}
# - set_b = {3, 4, 5, 6}
# 
# Encontre e imprima a interseção entre os dois conjuntos (os elementos que estão em ambos).

# %%
# Solução
set_a = {1,2,3,4}
set_b = {3,4,5,6}
print(set_a.intersection(set_b))

# %% [markdown]
# #### Exercício 30
# 
# Escreva um programa que peça ao usuário para digitar sua altura em metros (ex: 1.75) e seu peso em quilogramas (ex: 68.5). Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura * altura) e imprima o resultado formatado com duas casas decimais.

# %%
# Solução
altura = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu peso em Kg:'))

imc = peso / (altura**2)

print(f'Seu IMC é: {imc:.2f}')

# %% [markdown]
# # Fim


