# %% [markdown]
# Classificamos os 10 exercícios nas seguintes categorias:
# 
# - (Nível Baby)
# - (Nível Aprendiz)
# - (Nível Iniciante)
# - (Nível Iniciante Plus)
# - (Nível Pro)
# - (Nível Master)
# - (Nível Ninja)
# - (Nível Ninja Pro Master)
# - (Nível Ninja Pro Master das Galáxias)
# - (Nível Ninja Pro Master das Galáxias Plus)
# 
# Divirta-se. :-)

# %%
# Importa o NumPy
import numpy as np

# %% [markdown]
# #### Exercício 1: Selecionando uma Coluna Específica (Nível Baby)
# 
# Dado a matriz 4x4 abaixo, crie um novo array contendo apenas os elementos da terceira coluna.

# %%
# Cria a matriz
matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# %%
# Solução
terceira = matriz[:, 2]
print(terceira)

# Saída esperada: [ 3  7 11 15]

# %% [markdown]
# #### Exercício 2: Extraindo um Bloco (Submatriz) (Nível Aprendiz)
# 
# A partir da mesma matriz do exercício 1, extraia o bloco central 2x2, que contém os números 6, 7, 10 e 11.

# %%
# Solução
print(matriz[1:3, 1:3])


# Saída esperada:
# [[ 6  7]
#  [10 11]]

# %% [markdown]
# #### Exercício 3: Produto de Matrizes (Nível Iniciante)
# 
# Dadas as duas matrizes A e B abaixo, calcule o produto matricial entre A e B.

# %%
# Cria as matrizes
A = np.array([[1, 2, 3], [4, 5, 6]])       # Matriz 2x3
B = np.array([[7, 8], [9, 10], [11, 12]])  # Matriz 3x2

# %%
# Solução
produto = np.dot(A, B)
print(produto)
# Saída esperada:
# [[ 58  64]
#  [139 154]]

# %% [markdown]
# #### Exercício 4: Selecionando Linhas Pares e Colunas Ímpares (Nível Iniciante Plus)
# 
# Dada a matriz 9x9 abaixo, crie um novo array que contenha apenas os valores das linhas de índice par e as colunas de índice ímpar.

# %%
# Cria a matriz
matriz = np.arange(81).reshape(9, 9)
print(matriz)

# %%
# Solução
print(matriz[::2, 1::2])
# Saída esperada:
#[[ 1  3  5  7]
# [19 21 23 25]
# [37 39 41 43]
# [55 57 59 61]
# [73 75 77 79]]

# %% [markdown]
# #### Exercício 5: Somando Valor a Uma Submatriz (Nível Pro)
# 
# Dada a matriz abaixo (preenchida com zeros) adicione o valor 5 apenas ao bloco central 2x2.

# %%
# Cria a matriz
matriz = np.zeros((4, 4), dtype = int)

# %%
# Solução
matriz[1:3, 1:3] = 5
print(matriz)
# Saída esperada:
# [[0 0 0 0]
#  [0 5 5 0]
#  [0 5 5 0]
#  [0 0 0 0]]

# %% [markdown]
# #### Exercício 6: Normalização de Uma Matriz (Nível Master)
# 
# Normalize a matriz abaixo. 
# 
# A normalização (Z-score) é feita subtraindo a média de todos os elementos de cada elemento e, em seguida, dividindo pelo desvio padrão. 
# 
# Fórmula: (X - media) / desvio_padrao.

# %%
# Cria a matriz
matriz = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(matriz)

# %%
# Solução
media = np.mean(matriz)
desvio_padrao = np.std(matriz)

matriz_normalizada = (matriz - media) / desvio_padrao
print("Média:", media)
print("Desvio Padrão:", f"{desvio_padrao:.2f}")
print("\nMatriz Normalizada:")
print(np.round(matriz_normalizada, 2))

# %% [markdown]
# #### Exercício 7: Substituindo Valores com Base em Uma Condição (Nível Ninja)
# 
# Dada a matriz abaixo, crie uma nova matriz onde todos os números maiores que 8 sejam substituídos pelo valor -1. Crie uma cópia da matriz antes de fazer a operação.

# %%
# Cria a matriz
dados = np.arange(16).reshape(4, 4)
print(dados)

# %%
# Solução
dados[dados > 8] = -1
print(dados)

# Saída esperada:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8 -1 -1 -1]
#  [-1 -1 -1 -1]]

# %% [markdown]
# #### Exercício 8: Inversa de Uma Matriz (Nível Ninja Pro Master)
# 
# Calcule a matriz inversa da matriz A. Depois, verifique seu trabalho calculando o produto de A pela sua inversa (o resultado deve ser a matriz identidade).
# 
# A matriz inversa de uma matriz quadrada A é outra matriz, chamada A⁻¹, que quando multiplicada por A resulta na matriz identidade (uma matriz que tem 1 na diagonal principal e 0 nos outros elementos). Em outras palavras, A × A⁻¹ = I. A inversa só existe para matrizes quadradas que não sejam singulares, ou seja, que tenham determinante diferente de zero. Ela é usada para resolver sistemas lineares, desfazer transformações e em várias aplicações de álgebra linear.

# %%
# Cria a matriz
A = np.array([[4, 7], [2, 6]])
print(A)

# %%
# Solução
A_inversa = np.linalg.inv(A)
identidade = A @ A_inversa

print(A)
print(abs(np.round(A_inversa)))


# %% [markdown]
# #### Exercício 9: Resolvendo Um Sistema de Equações Lineares (Nível Ninja Pro Master das Galáxias)
# Resolva o seguinte sistema de equações lineares:
# 
# 2x + y = 8
# 
# x + 3y = 7
# 
# Represente o sistema na forma matricial Ax = b e encontre o vetor x (que contém os valores de x e y).

# %%
# Solução
A = np.array([[2, 1], [1,3]])

b = np.array([8, 7])

x = np.linalg.solve(A, b)
print(np.round(x, 2))
# Saída esperada: [3.4 1.2]

# %% [markdown]
# #### Exercício 10: Extraindo a Borda de Uma Matriz (Nível Ninja Pro Master das Galáxias Plus)
# 
# Dada uma matriz 5x5, crie um novo array 1D contendo todos os elementos da borda da matriz, em sentido horário, começando pelo canto superior esquerdo.

# %%
# Cria a matriz
matriz = np.arange(25).reshape(5, 5)
print(matriz)

# %%
# Solução
linha_topo = matriz[0, :]
linha_baixo = matriz[-1, :-1][::-1]
coluna_direita = matriz[1:, -1]
coluna_esquerda = matriz[1:-1, 0][::-1]

borda = np.concatenate((linha_topo, coluna_direita, linha_baixo, coluna_esquerda))
print(matriz)
print(borda)


# Saída esperada: [ 0  1  2  3  4  9 14 19 24 23 22 21 20 15 10  5]

# %% [markdown]
# # Fim


