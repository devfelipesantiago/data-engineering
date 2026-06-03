# %% [markdown]
# ## O Que é e Quando Usar o Pandas?

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## 1- Pandas e Estruturas de Dados - Series e DataFrame
# 
# Vamos começar criando as estruturas de dados fundamentais: Series e DataFrame.
# 
# No Pandas, uma Series (uma série) é uma estrutura unidimensional, parecida com uma coluna de uma tabela: contém uma sequência de valores com um índice associado. Já um DataFrame é uma estrutura bidimensional, semelhante a uma planilha, tabela ou matriz, formada por várias colunas (que são, internamente, Series alinhadas pelo mesmo índice).

# %%
# Criando uma Series (uma única coluna)
s = pd.Series([10, 20, 30, 40, 50], name = 'Valores')

# %%
type(s)

# %%
print("\n--- Exemplo de Series ---\n")
print(s)
print("\n")

# %%
# Criamos um dicionário em Python (observe que alguns valores estão nulos representados como None)
dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

# %%
type(dados)

# %%
print(dados)

# %%
# Convertemos o dicionário em um dataframe do pandas
df = pd.DataFrame(dados)

# %%
type(df)

# %%
print("\n--- Exemplo de DataFrame ---\n")
print(df)

# %% [markdown]
# ## 2- Leitura e Escrita de Dados no Formato CSV
# 
# Pandas torna muito fácil salvar seu DataFrame em um arquivo CSV e carregá-lo de volta.

# %%
# Escrevendo (salvando) o DataFrame em um arquivo CSV
# index=False evita que o índice do DataFrame seja salvo como uma coluna no CSV
df.to_csv('dados_funcionarios_sem_indice.csv', index = False, encoding = 'utf-8')

# %%
# Escrevendo (salvando) o DataFrame em um arquivo CSV
# index=True (valor padrão) inclui o índice do DataFrame como uma coluna no CSV
df.to_csv('dados_funcionarios_com_indice.csv', encoding = 'utf-8')

# %%
# Lendo dados de um arquivo CSV para um novo DataFrame
df_1 = pd.read_csv('dados_funcionarios_sem_indice.csv')

# %%
# Visualizando as primeiras linhas
df_1.head(6)

# %%
# Lendo dados de um arquivo CSV para um novo DataFrame
df_2 = pd.read_csv('dados_funcionarios_com_indice.csv')

# %%
# Visualizando as primeiras linhas
df_2.head(6)

# %%
# Deletando a coluna de índice 0
df_2 = df_2.drop(df_2.columns[0], axis = 1)

# %%
# Visualizando as primeiras linhas
df_2.head(6)

# %% [markdown]
# ## 3. Seleção e Indexação com Pandas
# 
# Existem várias maneiras de selecionar dados de um DataFrame. As mais comuns são loc (baseado em rótulo) e iloc (baseado em posição/índice numérico).

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Selecionando uma única coluna (retorna uma Series)
nomes = df['Nome']
print("\n--- Selecionando a coluna 'Nome' ---\n")
print(nomes)
print("\n")

# %%
type(nomes)

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Selecionando múltiplas colunas (retorna um DataFrame)
info_pessoal = df[['Nome', 'Idade']]
print("\n--- Selecionando as colunas 'Nome' e 'Idade' ---\n")
print(info_pessoal)
print("\n")

# %%
type(info_pessoal)

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Usando .loc para selecionar pela linha (rótulo/índice 1) e coluna ('Nome')
nome = df.loc[1, 'Nome']
print(f"\n--- Selecionando com .loc[1, 'Nome'] ---\n{nome}\n")

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Usando .iloc para selecionar pela posição da linha (linha 2) e da coluna (coluna 3)
salario_fabiana = df.iloc[2, 3]
print(f"\n--- Selecionando com .iloc[2, 3] ---\n{salario_fabiana}\n")

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Selecionando um intervalo de linhas
primeiras_tres_linhas = df.loc[0:2] # O final (2) é inclusivo com .loc
print("\n--- Selecionando as 3 primeiras linhas com .loc ---\n")
print(primeiras_tres_linhas)

# %% [markdown]
# ## 4. Filtragem de Dados com Pandas
# 
# Você pode filtrar linhas com base em condições lógicas, de forma muito intuitiva, bem como usar colunas como índice.

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Convertendo a coluna zero em índice
df = df.set_index(df.columns[0])

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Filtramos usando label do índice (linha) e da coluna
df.loc["Fabiana", "Salário"]

# %%
# Podemos aplicar o filtro de forma que retorne um dataframe. Observe a diferença sutil na sintaxe.
df.loc[["Fabiana"], ["Salário"]]

# %%
# Reset para retornar o índice ao padrão do Pandas
df = df.reset_index()

# %%
# Visualizando as primeiras linhas
df.head(6)

# %%
# Filtrando funcionários com idade superior a 30 anos
mais_de_30 = df[df['Idade'] > 30]
print("\n--- Funcionários com mais de 30 anos ---\n")
print(mais_de_30)
print("\n")

# %%
# Filtrando funcionários de São Paulo com salário acima de 6000
sp_salario_alto = df[(df['Cidade'] == 'São Paulo') & (df['Salário'] > 6000)]
print("\n--- Funcionários de São Paulo com salário > 6000 ---\n")
print(sp_salario_alto)

# %%
# Verificamos quais células têm valores nulos
df.isnull()

# %%
# Verificamos se há qualquer valor nulo em cada coluna
df.isnull().any()

# %%
# Retorna apenas as colunas que possuem pelo menos um valor nulo
df_colunas_com_nulos = df.loc[:, df.isnull().any()]

# %%
df_colunas_com_nulos.head()

# %%
# Retorna apenas linhas com valores nulos
df_linhas_com_nulos = df[df.isnull().any(axis = 1)]

# %%
df_linhas_com_nulos.head()

# %%
# Podemos ainda filtrar pela coluna e então verificar se há valores nulos
linhas_com_nulos_idade = df[df["Idade"].isnull()]

# %%
linhas_com_nulos_idade.head()

# %% [markdown]
# ## 5. Inspeção de DataFrames do Pandas
# 
# Podemos inspecionar e resumir o dataframe de várias formas.

# %%
# Mostra o número de linhas e colunas (formato)
print(f"\n--- Formato do DataFrame (.shape) ---\n{df.shape}")

# %%
# Mostra as 3 primeiras linhas do DataFrame
print("\n--- As 3 primeiras linhas (.head(3)) ---\n")
print(df.head(3))
print("\n")

# %%
# Mostra as 2 últimas linhas do DataFrame
print("\n--- As 2 últimas linhas (.tail(2)) ---\n")
print(df.tail(2))
print("\n")

# %%
# Fornece um resumo conciso do DataFrame (tipos de dados, valores não nulos, etc.)
# Observe a contagem de valores
print("\n--- Informações gerais (.info()) ---\n")
df.info()
print("\n")

# %%
# Gera estatísticas descritivas das colunas numéricas
print("\n--- Estatísticas descritivas (.describe()) ---\n")
print(df.describe())
print("\n")

# %%
print("\n--- Estatísticas descritivas (numéricas e objetos) ---\n")
print(df.describe(include = 'all'))  # inclui números, objetos e categorias

# %%
df.describe(include = [object])   # só colunas do tipo object

# %%
df.describe(include = [np.number])  # só colunas numéricas (comportamento padrão)

# %% [markdown]
# ## 6. Operações e Transformações de Dados com Pandas
# 
# Você pode facilmente criar novas colunas a partir de outras ou aplicar funções para modificar os dados. Fazemos isso com frequência em tarefas de engenharia de atributos em projetos de Ciência de Dados.

# %%
df.head(6)

# %%
# Criando uma nova coluna 'Salário Anual'
df['Salário Anual'] = df['Salário'] * 12
print("\n--- DataFrame com a nova coluna 'Salário Anual' ---\n")
print(df)
print("\n")

# %%
# Aplicando uma função para criar uma coluna de bônus
# A função lambda aplica a operação para cada valor na coluna 'Salário'
df['Bônus'] = df['Salário'].apply(lambda x: x * 0.10 if x > 7000 else x * 0.05)
print("\n--- DataFrame com a nova coluna 'Bônus' ---\n")
print(df)

# %% [markdown]
# Vamos criar uma coluna de faixa etária.

# %%
# Define as condições (vamos criar o que chamamos de máscara)
condicoes = [
    df['Idade'] < 18,
    (df['Idade'] >= 18) & (df['Idade'] <= 30),
    (df['Idade'] > 30) & (df['Idade'] <= 60),
    df['Idade'] > 60
]

# %%
print(condicoes)

# %%
# Define os rótulos correspondentes
faixas = ['Menor de idade', 'Jovem', 'Adulto', 'Idoso']

# %%
# Cria a nova coluna
df['Faixa Etária'] = np.select(condicoes, faixas, default = 'Idade não informada')

# %%
df.head(6)

# %% [markdown]
# ## 7. Agrupamento de Dados (Group By) com Pandas
# 
# O método groupby é extremamente poderoso para análises segmentadas. É exatamente o mesmo conceito usado em Linguagem SQL.

# %%
df.head(6)

# %%
# Agrupando os dados por 'Cidade' e calculando a média de 'Salário' para cada cidade
media_salario_cidade = df.groupby('Cidade')['Salário'].mean()
print("\n--- Média de Salário por Cidade ---\n")
print(np.round(media_salario_cidade,2))
print("\n")

# %%
# Agrupando por cidade e calculando múltiplas agregações
agregacao_cidade = df.groupby('Cidade').agg(Media_Salarial = ('Salário', 'mean'),
                                                Idade_Maxima = ('Idade', 'max'),
                                                Contagem = ('Nome', 'count'))

# %%
print("\n--- Agregação múltipla por Cidade ---\n")
print(agregacao_cidade)

# %% [markdown]
# ## 8. Manipulação de Tipos de Dados com Pandas
# 
# Garantir que cada coluna tenha o tipo de dado correto é fundamental para qualquer tipo de análise.

# %%
# Verificando os tipos de dados atuais
print("\n--- Tipos de dados antes da conversão ---\n")
print(df.dtypes)
print("\n")

# %%
# Convertendo a coluna 'Idade' de float64 para int64 - ATENÇÃO!!!!!
#df['Idade'] = df['Idade'].astype(int)

# %%
# Primeiro removemos a linha com valor ausente
df = df.dropna(subset = ['Idade'])

# E então fazemos a conversão
df['Idade'] = df['Idade'].astype(int)

# %%
print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

# %%
# Convertendo do tipo object para o tipo string
df['Nome'] = df['Nome'].astype('string')
df['Cidade'] = df['Cidade'].astype('string')
df['Faixa Etária'] = df['Faixa Etária'].astype('string')

# %%
print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

# %%
# Converte todas as colunas do tipo object para string
df = df.astype({col: 'string' for col in df.select_dtypes(include = 'object').columns})

# %%
print("\n--- Tipos de dados após a conversão ---\n")
print(df.dtypes)

# %% [markdown]
# Diferença entre object e string no pandas:
# 
# - object é um tipo genérico que armazena qualquer coisa em Python (strings, números, listas, etc.).
# 
# - string (desde o Pandas 1.0) é um tipo de dado nativo para texto, pensado para operações mais seguras e consistentes com strings.
# 
# Com string, você ganha melhor integração com métodos de texto (.str) e tratamento explícito de valores ausentes (< NA > em vez de NaN misturado com objetos).
# 
# Em grandes DataFrames, o tipo string pode ser um pouco mais eficiente e evita confusões quando colunas deveriam ser só texto. Mas não é obrigatório converter, mas usar string ajuda a ter consistência, evitar misturar tipos diferentes na mesma coluna e facilita operações textuais. Para análises e limpeza de dados de texto, geralmente vale a pena.

# %% [markdown]
# ## 9. Criação de Tabelas Dinâmicas (Pivot Tables) com Pandas
# 
# Tabelas dinâmicas são ótimas para resumir dados de forma semelhante a uma planilha.

# %%
# Vamos adicionar mais dados para a tabela dinâmica ficar mais interessante
dados_vendas = {
    'Data': pd.to_datetime(['2026-09-01', '2026-09-01', '2026-09-02', '2026-09-02', '2026-09-01']),
    'Região': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte'],
    'Vendedor': ['Carlos', 'Ana', 'Carlos', 'Ana', 'Pedro'],
    'Vendas': [250, 300, 150, 400, 200]
}

# %%
# Cria o dataframe
df_vendas = pd.DataFrame(dados_vendas)

# %%
df_vendas

# %%
df_vendas.dtypes

# %%
# Criando uma tabela dinâmica para ver o total de vendas por Região e Vendedor
tabela_dinamica = df_vendas.pivot_table(values = 'Vendas', 
                                        index = 'Região', 
                                        columns = 'Vendedor', 
                                        aggfunc = 'sum', 
                                        fill_value = 0)

# %%
print("\n--- Tabela Dinâmica: Total de Vendas por Região e Vendedor ---\n")
tabela_dinamica

# %% [markdown]
# ## 10. Visualizações de Dados com Pandas e Matplotlib
# 
# O Pandas se integra perfeitamente com o Matplotlib para criar visualizações diretamente do DataFrame.

# %%
# É uma boa prática executar este comando em notebooks Jupyter
# para garantir que os gráficos apareçam inline
%matplotlib inline

# %%
# Carrega novamente o dataframe inicial
df = pd.read_csv('dados_funcionarios_sem_indice.csv')

# %%
df

# %%
# Calcula a média de salário por cidade
media_salario_cidade = df.groupby('Cidade')['Salário'].mean()

# %%
type(media_salario_cidade)

# %%
# Gráfico de Barras: Média de Salário por Cidade
media_salario_cidade.plot(kind = 'bar', figsize = (12, 5), color = 'skyblue')

# Adicionando títulos e rótulos
plt.title('Média Salarial Por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Média de Salário (R$)')
plt.xticks(rotation = 45) 
plt.grid(axis = 'y', linestyle = '--')

# Mostra o gráfico
plt.show()

# %%
# Contagem de registros (funcionários) por cidade
contagem_cidade = df['Cidade'].value_counts()

# %%
type(contagem_cidade)

# %%
contagem_cidade

# %%
# Gráfico de Pizza: Contagem de funcionários por cidade
contagem_cidade.plot(kind = 'pie', autopct = '%1.1f%%', figsize = (6, 6), startangle = 90)
plt.title('Distribuição de Funcionários Por Cidade')
plt.ylabel('') # Remove o rótulo do eixo y
plt.show()


