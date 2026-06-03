# %%
# Imports
import pandas as pd
import numpy as np

# %% [markdown]
# #### Exercício 1: Seleção de Dados Condicional
# 
# A partir do DataFrame de funcionários abaixo, selecione e exiba apenas os funcionários do departamento de 'Vendas' que têm um salário superior a R$ 4.500.

# %%
# Dados de exemplo
dados = {'Nome': ['Ana', 'Bruno', 'Carla', 'Matias', 'Eliana', 'Fabiano'],
         'Departamento': ['RH', 'Vendas', 'TI', 'Vendas', 'RH', 'Vendas'],
         'Salário': [4000, 5000, 6200, 4400, 4300, 5500]}

# %%
# DataFrame
df_funcionarios = pd.DataFrame(dados)

# %%
df_funcionarios

# %%
# Solução
depto = df_funcionarios['Departamento'] == 'Vendas'
salario = df_funcionarios['Salário'] > 4500
funcionarios = df_funcionarios[depto & salario]

funcionarios

# %% [markdown]
# #### Exercício 2: Agrupamento e Agregação (groupby)
# 
# Com o DataFrame de vendas abaixo, calcule o total de vendas (Valor) para cada categoria de produto.

# %%
# Dados de exemplo
dados_vendas = {'Categoria': ['Eletrônicos', 'Vestuário', 'Eletrônicos', 'Casa', 'Vestuário', 'Eletrônicos'],
                'Produto': ['TV', 'Camiseta', 'Notebook', 'Sofá', 'Calça', 'Celular'],
                'Valor': [2500, 80, 4500, 1500, 120, 3000]}

# %%
# DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# %%
df_vendas

# %%
# Solução
total_vendas = df_vendas.groupby('Categoria')['Valor'].sum()
print(total_vendas)

# %% [markdown]
# #### Exercício 3: Criação de Nova Coluna
# A partir do DataFrame de produtos abaixo, crie uma nova coluna chamada Preco_com_Desconto que contenha o valor da coluna Preco com 10% de desconto.

# %%
# Dados de exemplo
dados_produtos = {'Produto': ['Monitor', 'Teclado', 'Mouse', 'Webcam'],
                  'Preco': [800, 120, 70, 250]}

# %%
# DataFrame
df_produtos = pd.DataFrame(dados_produtos)

# %%
df_produtos

# %%
# Solução
df_produtos['Preco_com_Desconto'] = df_produtos['Preco'] * 0.9
df_produtos

# %% [markdown]
# #### Exercício 4: Tratamento de Dados Ausentes (NaN)
# 
# No DataFrame de alunos abaixo, substitua as notas ausentes (NaN) pela média da turma (média da coluna 'Nota').

# %%
# Dados de exemplo
dados_alunos = {'Aluno': ['Alice', 'Bernardo', 'Clara', 'Marcelo'],
                'Nota': [8.5, 7.0, np.nan, 9.0]}

# %%
# DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# %%
df_alunos

# %%
# Solução
media = df_alunos['Nota'].mean()
print(f'Média das notas (ignorando NaN): {media}')
df_alunos['Nota'].fillna(media, inplace=True)
df_alunos

# %% [markdown]
# #### Exercício 5: Ordenação de Dados (sort_values)
# 
# Ordene o DataFrame de pontuações abaixo, do maior para o menor com base na coluna 'Pontos' e exiba o resultado.

# %%
# Dados de exemplo
dados_pontuacao = {'Jogador': ['J1', 'J2', 'J3', 'J4', 'J5'],
                   'Pontos': [88, 95, 74, 102, 95]}

# %%
# DataFrame
df_pontuacao = pd.DataFrame(dados_pontuacao)

# %%
df_pontuacao

# %%
# Solução
df_pontuacao_sorted = df_pontuacao.sort_values(by='Pontos', ascending=False)
df_pontuacao_sorted

# %% [markdown]
# #### Exercício 6: Combinação de DataFrames (merge)
# 
# Combine os DataFrames df_clientes e df_pedidos com base na coluna em comum ID_Cliente.

# %%
# Dados de exemplo
df_clientes = pd.DataFrame({'ID_Cliente': [1, 2, 3],
                            'Nome': ['Carlos', 'Mariana', 'Lucas']})

# %%
# Dados de exemplo
df_pedidos = pd.DataFrame({'ID_Pedido': [101, 102, 103, 104],
                           'ID_Cliente': [2, 1, 2, 3],
                           'Produto': ['Livro', 'Caneta', 'Caderno', 'Mochila']})

# %%
# Solução
df_combinado = pd.merge(df_clientes, df_pedidos, on='ID_Cliente')
df_combinado

# %% [markdown]
# #### Exercício 7: Manipulação de Strings (.str)
# No DataFrame abaixo, extraia o ano da coluna Data e crie uma nova coluna chamada Ano.

# %%
# Dados de exemplo
dados_eventos = {'Evento': ['Conferência A', 'Workshop B', 'Feira C'],
                 'Data': ['2025-10-25', '2026-03-12', '2026-09-01']}

# %%
# DataFrame
df_eventos = pd.DataFrame(dados_eventos)

# %%
df_eventos

# %%
# Solução
df_eventos['Ano'] = pd.to_datetime(df_eventos['Data']).dt.year
print(df_eventos)

# %% [markdown]
# #### Exercício 8: Uso do Método apply
# 
# Crie uma nova coluna Status no DataFrame de notas. Se a Nota for maior ou igual a 7, o status deve ser 'Aprovado', caso contrário, 'Reprovado'. Use o método apply.

# %%
# Dados de exemplo
dados_notas = {'Aluno': ['Maria', 'Jeremias', 'Paulo', 'Roberto'],
               'Nota': [9.5, 6.0, 5.5, 8.0]}

# %%
# DataFrame
df_notas = pd.DataFrame(dados_notas)

# %%
df_notas

# %%
# Solução
df_notas['Status'] = df_notas['Nota'].apply(lambda nota: 'Aprovado' if nota >= 7 else 'Reprovado')
print(df_notas)

df_notas_np = np.where(df_notas['Nota'] >= 7, 'Aprovado', 'Reprovado')


# %% [markdown]
# #### Exercício 9: Criação de Tabela Dinâmica (pivot_table)
# Crie uma tabela dinâmica que mostre a soma das Vendas por Regiao e Vendedor.

# %%
# Dados de exemplo
dados_regional = {'Regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
                  'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Carlos', 'Bruno'],
                  'Vendas': [1000, 1500, 1200, 1800, 800, 1300]}

# %%
# DataFrame
df_regional = pd.DataFrame(dados_regional)

# %%
df_regional

# %%
# Solução
df_pivot = df_regional.pivot_table(index='Regiao', columns='Vendedor', values='Vendas', aggfunc='sum', fill_value=0)
print(df_pivot)

# %% [markdown]
# #### Exercício 10: Análise de Séries Temporais
# 
# A partir do DataFrame de visitas a um site, selecione e exiba apenas os registros do mês de agosto de 2026.

# %%
# Dados de exemplo
datas = pd.to_datetime(pd.date_range(start = '2026-07-25', periods = 15, freq = 'D'))
dados_visitas = {'Visitas': [150, 165, 178, 199, 205, 210, 225, 230, 215, 240, 255, 260, 245, 250, 270]}
df_visitas = pd.DataFrame(data = dados_visitas, index = datas)
df_visitas.index.name = 'Data'

# %%
df_visitas

# %%
# Solução
eventos_26 = df_visitas[df_visitas.index.month == 8]
# Para selecionar linhas com base no índice, usamos o .loc
visitas = df_visitas.loc['2026-08']
visitas
eventos_26


