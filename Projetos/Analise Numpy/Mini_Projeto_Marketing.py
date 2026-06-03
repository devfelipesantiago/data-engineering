# %% [markdown]
# ## 1. Definição do Problema de Negócio

# %% [markdown]
# ### 1.1. Contexto
# 
# Uma plataforma de e-commerce coleta um volume significativo de dados sobre a interação dos usuários com o site, incluindo o número de visitas, a duração da sessão, a atividade de adição de produtos ao carrinho e os valores de compra finalizados. No entanto, esses dados estão sendo subutilizados. Atualmente, as decisões sobre campanhas de marketing, promoções e melhorias na experiência do usuário (UX) são tomadas com base em intuição e métricas de alto nível, sem uma compreensão aprofundada dos padrões de comportamento que impulsionam os resultados.
# 
# ### 1.2. Problema de Negócio
# 
# A empresa enfrenta o desafio de compreender profundamente os padrões de comportamento que diferenciam os clientes de alto valor dos visitantes que abandonam o site sem comprar. Essa falta de clareza resulta em:
# 
# - Marketing Genérico: Nossas campanhas de marketing são de "tamanho único", resultando em baixo engajamento e desperdício de orçamento, pois não conseguimos personalizar as ofertas para os segmentos de clientes corretos.
# 
# - Perda de Oportunidades: Não conseguimos identificar e engajar proativamente os clientes com maior potencial de compra ou criar estratégias para converter os visitantes que demonstram interesse, mas não finalizam a compra.
# 
# - Decisões Não Embasadas: As estratégias de produto e de experiência do usuário carecem de uma base quantitativa sólida sobre quais comportamentos (ex: tempo no site, frequência de visitas) estão mais fortemente correlacionados com o sucesso das vendas.
# 
# ### 1.3. Objetivo Principal
# 
# Utilizar a análise estatística dos dados de navegação e compra para segmentar clientes, identificar os principais indicadores de comportamento que levam à conversão e fornecer insights acionáveis para as equipes de marketing e produto, a fim de aumentar o ticket médio e a taxa de conversão geral da plataforma.
# 
# ### 1.4. Perguntas-Chave a Serem Respondidas
# 
# A análise de dados deve responder às seguintes perguntas críticas de negócio:
# 
# - 1- Qual é o perfil médio do nosso usuário em termos de visitas, tempo de navegação e valor de compra (ticket médio)?
# 
# - 2- Quais são as características e comportamentos distintos dos nossos clientes de "Alto Valor"? Eles visitam mais o site? Passam mais tempo navegando?
# 
# - 3- Qual é o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra? Onde está a oportunidade de conversão com este grupo?
# 
# - 4- Existe uma correlação estatisticamente relevante entre o tempo gasto no site, o número de itens no carrinho e o valor final da compra?
# 
# ### 1.5. Resultado Esperado e Impacto no Negócio
# 
# O resultado deste projeto será um relatório de análise estatística que permitirá:
# 
# - Segmentação Aprimorada: Criação de pelo menos dois segmentos de clientes (ex: "Clientes de Alto Valor" e "Visitantes Engajados sem Compra") para direcionamento de campanhas de marketing personalizadas.
# 
# - Otimização de Marketing: Direcionar o orçamento de marketing para ações focadas nos comportamentos que mais se correlacionam com compras de alto valor, aumentando o Retorno Sobre o Investimento (ROI).
# 
# - Melhoria da Experiência do Usuário (UX): Fornecer à equipe de produto dados que possam justificar testes A/B ou melhorias em áreas do site frequentadas por usuários que não convertem.

# %% [markdown]
# ## 2. Importação das Bibliotecas

# %%
# Importando a biblioteca NumPy
import numpy as np

# %%
# Outros Imports
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Definir uma semente para reprodutibilidade dos resultados
np.random.seed(42)

# %%
# Definir o número de usuários
num_usuarios = 500

# %%
# 1. Gerar o número de visitas (entre 1 e 50)
visitas = np.random.randint(1, 51, size = num_usuarios)

# %% [markdown]
# A distribuição normal é um tipo de distribuição de probabilidade contínua, simétrica em torno da média, com formato característico de sino. Nesse tipo de distribuição os valores próximos da média são mais frequentes e a probabilidade de observar valores extremos diminui gradualmente conforme se afastam do centro. É definida por dois parâmetros: a média (que indica o centro da distribuição) e o desvio padrão (que indica a dispersão dos dados). É muito usada em Estatística e Ciência de Dados porque muitos fenômenos naturais e sociais tendem a seguir esse padrão.

# %%
# 2. Gerar o tempo no site (distribuição normal, correlacionado com as visitas)
# Média de 20 min, desvio padrão de 5, com um bônus por visita
tempo_no_site = np.random.normal(loc = 20, scale = 5, size = num_usuarios) + (visitas * 0.5)
tempo_no_site = np.round(tempo_no_site, 2) # Arredondar para 2 casas decimais

# %%
# 3. Gerar o número de itens no carrinho (dependente das visitas e do tempo)
# Usuários que visitam mais e passam mais tempo, tendem a adicionar mais itens
itens_no_carrinho = np.random.randint(0, 8, size = num_usuarios) + (visitas // 10)

# %%
# Garante que o tempo no site também influencie positivamente
itens_no_carrinho = (itens_no_carrinho + (tempo_no_site // 15)).astype(int)

# %%
# 4. Gerar o valor da compra (correlacionado com os itens no carrinho)
# Preço médio por item de R$ 35, com alguma variação aleatória
valor_compra = (itens_no_carrinho * 35) + np.random.normal(loc = 0, scale = 10, size = num_usuarios)

# %%
type(valor_compra)

# %%
type(itens_no_carrinho)

# %%
# Se não houver itens no carrinho, o valor da compra deve ser 0
valor_compra[itens_no_carrinho == 0] = 0
valor_compra[valor_compra < 0] = 0 # Corrigir valores negativos que possam surgir
valor_compra = np.round(valor_compra, 2)

# %%
# Unindo tudo em uma única matriz (ndarray)
# Cada linha representa um usuário, cada coluna uma métrica
dados_ecommerce = np.column_stack((visitas, tempo_no_site, itens_no_carrinho, valor_compra))

# %%
print("\nShape da nossa massa de dados:", dados_ecommerce.shape)
print("\nExemplo dos 5 primeiros usuários (linhas):")
print("\nColunas: [Visitas, Tempo no Site (min), Itens no Carrinho, Valor da Compra (R$)]\n")
print(dados_ecommerce[:5])

# %% [markdown]
# ## 4. Análise Estatística Descritiva
# 
# Agora que temos os dados, vamos calcular as principais métricas estatísticas para cada coluna para ter uma visão geral do comportamento dos nossos usuários.
# 
# - A média é a soma de todos os valores dividida pela quantidade de elementos. Ela indica o valor “central” ou típico de um conjunto de dados.
# 
# - A mediana é o valor que fica exatamente no meio quando os dados estão ordenados. Se houver um número par de valores, é a média dos dois valores centrais. Ela é menos sensível a valores muito extremos do que a média.
# 
# - O desvio padrão mede o quanto os valores se afastam, em média, da média do conjunto. Um desvio padrão alto significa que os dados são mais espalhados; um baixo indica que estão mais próximos da média.
# 
# ### Pergunta 1
# 
# Qual é o perfil médio do nosso usuário em termos de visitas, tempo de navegação e valor de compra (ticket médio)?

# %%
# Separando as colunas para facilitar a leitura do código
visitas_col = dados_ecommerce[:, 0]
tempo_col   = dados_ecommerce[:, 1]
itens_col   = dados_ecommerce[:, 2]
valor_col   = dados_ecommerce[:, 3]

print("--- ANÁLISE ESTATÍSTICA GERAL ---")

# Média
media_visitas = np.mean(visitas_col)
media_tempo   = np.mean(tempo_col)
media_itens   = np.mean(itens_col)
media_valor   = np.mean(valor_col)

print(f"\nMédia de Visitas: {media_visitas:.2f}")
print(f"Média de Tempo no Site: {media_tempo:.2f} min")
print(f"Média de Itens no Carrinho: {media_itens:.2f}")
print(f"Média de Valor de Compra (Ticket Médio): R$ {media_valor:.2f}")

# Mediana (valor central, menos sensível a outliers)
mediana_valor = np.median(valor_col)
print(f"\nMediana do Valor de Compra: R$ {mediana_valor:.2f}")

# Desvio Padrão (mede a dispersão dos dados)
std_valor = np.std(valor_col)
print(f"Desvio Padrão do Valor de Compra: R$ {std_valor:.2f}")

# Valores Máximos e Mínimos
max_valor = np.max(valor_col)
min_valor_positivo = np.min(valor_col[valor_col > 0]) # Mínimo apenas entre quem comprou
print(f"Maior Valor de Compra: R$ {max_valor:.2f}")
print(f"Menor Valor de Compra (de quem comprou): R$ {min_valor_positivo:.2f}")

# %% [markdown]
# Este gráfico abaixo mostra o histograma dos valores de compra com linhas verticais indicando a média (vermelho), a mediana (laranja) e o intervalo de um desvio padrão acima e abaixo da média (linhas verdes). Isso facilita a análise de como os dados estão distribuídos e se existem possíveis outliers ou assimetrias.

# %%
# Separando colunas
visitas_col = dados_ecommerce[:, 0]
tempo_col   = dados_ecommerce[:, 1]
itens_col   = dados_ecommerce[:, 2]
valor_col   = dados_ecommerce[:, 3]

# Calculando as Estatísticas
media_valor = np.mean(valor_col)
mediana_valor = np.median(valor_col)
std_valor = np.std(valor_col)

# --- GRÁFICO ---
plt.figure(figsize = (12, 5))
plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = '--', linewidth = 2, label = f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

# %% [markdown]
# **Resposta da Pergunta 1:**
# 
# O usuário acessa o site, em média, cerca de 26 vezes por mês, permanece em média 33 minutos navegando, adiciona aproximadamente 7 itens ao carrinho e realiza compras com ticket médio de R$ 252,70. 
# 
# O gasto típico fica próximo da mediana de R$ 248,13.
# 
# Mas há grande variação entre clientes, alguns compram valores baixos a partir de R$ 23,42. 
# 
# Enquanto outros chegam a gastar até R$ 530,37.

# %% [markdown]
# ## 5. Segmentação e Análise de Clientes
# 
# Vamos usar a indexação booleana para filtrar e analisar segmentos específicos de clientes.

# %% [markdown]
# ### Pergunta 2
# 
# Quais são as características e comportamentos distintos dos nossos clientes de "Alto Valor"? Eles visitam mais o site? Passam mais tempo navegando?

# %%
# Filtro booleano para clientes com compras > R$ 250
clientes_alto_valor = dados_ecommerce[dados_ecommerce[:, 3] > 250]

print("\n--- ANÁLISE: CLIENTES DE ALTO VALOR (Compras > R$ 250) ---\n")
print(f"Número de clientes de alto valor: {clientes_alto_valor.shape[0]}")

# Estatísticas deste segmento
media_visitas_alto_valor = np.mean(clientes_alto_valor[:, 0])
media_tempo_alto_valor = np.mean(clientes_alto_valor[:, 1])

print(f"Média de visitas desses clientes: {media_visitas_alto_valor:.2f}")
print(f"Média de tempo no site desses clientes: {media_tempo_alto_valor:.2f} min")

# %% [markdown]
# **Resposta da Pergunta 2:**
# 
# Os clientes de alto valor (aqueles que gastam mais de R$ 250) visitam o site com maior frequência, em média 33 vezes por mês, e permanecem mais tempo navegando, cerca de 37 minutos por sessão. Esse comportamento indica um alto nível de engajamento, sugerindo que quanto mais esses usuários interagem com a plataforma, maior tende a ser o valor de suas compras.

# %% [markdown]
# ### Pergunta 3
# 
# Qual é o comportamento dos usuários que visitam o site, mas não realizam nenhuma compra? Onde está a oportunidade de conversão com este grupo?

# %%
# Filtro para visitantes que não compraram
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]

print("\n--- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compraram: {visitantes_sem_compra.shape[0]}")

# Estatísticas deste segmento
media_tempo_sem_compra = np.mean(visitantes_sem_compra[:, 1])
media_visitas_sem_compra = np.mean(visitantes_sem_compra[:, 0])

print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min no site.")

# %% [markdown]
# **Resposta da Pergunta 3:**
# 
# Os usuários que não realizam compras visitam o site em média 7 vezes e permanecem cerca de 15 minutos navegando, mas não finalizam nenhuma transação. Esse comportamento mostra que, mesmo com algum nível de interesse, eles acabam desistindo antes da compra, representando uma oportunidade para ações de remarketing, otimização do checkout e estratégias de incentivo, como descontos ou frete grátis, para aumentar a conversão.

# %% [markdown]
# ## Análise de Correlação
# 
# Vamos investigar a relação entre as diferentes variáveis. Uma matriz de correlação nos mostra como as variáveis se movem juntas.
# 
# - +1: Correlação positiva perfeita
# - -1: Correlação negativa perfeita
# - 0: Nenhuma correlação linear
# 
# ### Pergunta 4
# 
# Existe uma correlação estatisticamente relevante entre o tempo gasto no site, o número de itens no carrinho e o valor final da compra?

# %%
# A função np.corrcoef calcula a matriz de correlação
# rowvar=False indica que as colunas são as variáveis
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)

print("\n--- MATRIZ DE CORRELAÇÃO ---\n")
print("[Visitas, Tempo, Itens, Valor]\n")
print(np.round(matriz_correlacao, 2))

# %% [markdown]
# <!-- Trabalho Desenvolvido no Curso da Data Science Academy - www.datascienceacademy.com.br -->
# Vamos melhorar isso e colocar a matriz de correlação de forma gráfica.

# %%
# Calcula a matriz de correlação
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)

# Define os nomes das variáveis
nomes_variaveis = ["Visitas", "Tempo no Site", "Itens no Carrinho", "Valor da Compra"]

# Converte em DataFrame para exibir com rótulos
df_correlacao = pd.DataFrame(matriz_correlacao, 
                             index = nomes_variaveis, 
                             columns = nomes_variaveis)

# Matriz de correlação (mapa de calor)
plt.figure(figsize = (7, 5))
sns.heatmap(df_correlacao, annot = True, cmap = "Blues", fmt = ".2f")
plt.title("Matriz de Correlação")
plt.show()

# %% [markdown]
# **Resposta da Pergunta 4:**
# 
# A matriz está organizada na ordem [Visitas, Tempo, Itens, Valor]. Os valores variam entre –1 e +1, onde:
# 
# - +1 indica correlação positiva perfeita
# - 0 indica ausência de correlação
# - –1 indica correlação negativa perfeita
# 
# No trecho relevante para a pergunta:
# 
# - Tempo ↔ Valor = 0,59 → correlação positiva moderada
# 
# - Itens ↔ Valor = 1,00 → correlação positiva perfeita (neste conjunto de dados, valor cresce proporcionalmente ao número de itens)
# 
# - Tempo ↔ Itens = 0,60 → correlação positiva moderada
# 
# Esses números indicam que quanto mais tempo o usuário passa no site, maior tende a ser o número de itens no carrinho e, consequentemente, maior o valor da compra. O fato de “Itens ↔ Valor” ser 1,00 mostra que, no dataset analisado, o valor final cresce linearmente com a quantidade de itens (possivelmente porque cada item tem preço médio semelhante).
# 
# Assim, a resposta para a pergunta seria:
# 
# - Sim. Há uma correlação estatisticamente relevante: o tempo gasto no site se relaciona moderadamente tanto com o número de itens no carrinho quanto com o valor final da compra, e a quantidade de itens tem correlação praticamente perfeita com o valor final, indicando forte relação entre esses fatores.
# 
# Obs: Para confirmar a significância estatística, seria necessário calcular o p-valor dessas correlações.

# %% [markdown]
# ## Passo 6: Relatório Final, Conclusões e Insights a Partir dos Dados
# 
# A análise estatística dos dados de navegação e compras dos usuários do e-commerce permitiu compreender melhor o comportamento dos clientes e identificar padrões diretamente relacionados à geração de receita.
# 
# **1. Perfil Geral dos Usuários**
# 
# Os usuários acessam a plataforma em média 25,86 vezes por mês, permanecendo cerca de 32,78 minutos no site por sessão. Cada cliente adiciona, em média, 7,20 itens ao carrinho e realiza compras com ticket médio de R$ 252,70. 
# 
# A mediana do valor gasto é de R$ 248,13. 
# 
# Isso indica que metade dos clientes compra abaixo e metade acima desse valor. Observou-se uma dispersão considerável nos gastos (desvio padrão de R$ 106,94). As compras variam de 23,42 (mínimo) a 530,37 (máximo registrado).
# 
# Esses números mostram que existe um grupo expressivo de consumidores que gasta significativamente mais que a média, mas também há grande variação no comportamento de compra.
# 
# **2. Clientes de Alto Valor**
# 
# Ao analisar os clientes que gastam mais de R$ 250, identificou-se um total de 245 usuários, representando aproximadamente metade da base analisada. Este grupo se destaca por visitar mais vezes o site (33,29 visitas em média) e permanecer por mais tempo (37,11 minutos), comparado ao perfil geral.
# Isso sugere que engajamento elevado, tanto em frequência de visitas quanto em tempo de navegação, está fortemente associado a compras de maior valor. Esses clientes podem ser considerados um segmento prioritário para ações de fidelização, programas de recompensa e campanhas personalizadas.
# 
# **3. Visitantes Que Não Compram**
# 
# Foi identificado apenas 1 usuário que navega sem realizar compras. Apesar de representar um caso isolado nesta base, ele visita em média 7 vezes e permanece 14,71 minutos no site. Esse comportamento, mesmo pouco expressivo aqui, ilustra a importância de monitorar usuários engajados que não convertem, pois podem representar oportunidades para campanhas de remarketing, melhorias no processo de checkout ou incentivos específicos para concluir a compra.
# 
# **4. Relações Entre Comportamentos e Receita**
# 
# A matriz de correlação revelou informações valiosas:
# 
# - Itens no Carrinho ↔ Valor da Compra = 1,00 → correlação positiva perfeita; cada item adicional impacta diretamente o valor gasto.
# 
# - Tempo no Site ↔ Itens no Carrinho = 0,60 → correlação moderada; usuários que permanecem mais tempo tendem a adicionar mais itens.
# 
# - Tempo no Site ↔ Valor da Compra = 0,59 → correlação moderada; quanto mais tempo no site, maior tende a ser a compra.
# 
# - Visitas ↔ Valor da Compra = 0,65 → correlação positiva; maior frequência de acessos também contribui para compras maiores.
# 
# Esses resultados confirmam que engajamento do usuário (tempo e visitas) influencia a construção do carrinho e, consequentemente, o valor final da compra. Embora seja necessário confirmar a significância estatística com testes adicionais (p-valor), a força das correlações já orienta decisões estratégicas.
# 
# **5. Conclusões e Recomendações**
# 
# - Segmentação estratégica: os clientes de alto valor apresentam comportamento diferenciado, com maior frequência e tempo de navegação. Esse grupo deve ser alvo de campanhas personalizadas e programas de fidelidade para aumentar retenção e ticket médio.
# 
# - Incentivo à construção de carrinho: como a quantidade de itens é fator determinante no valor gasto, estratégias como recomendações personalizadas, descontos progressivos e combos podem elevar o ticket médio.
# 
# - Aproveitamento de visitantes engajados sem compra: embora pouco representativo aqui, vale investir em remarketing e otimização de UX para reduzir fricções no checkout e converter quem demonstra interesse.
# 
# - Base quantitativa para decisões: a análise estatística mostra que dados simples (visitas, tempo, itens) já oferecem insights poderosos para melhorar campanhas de marketing e decisões de produto, substituindo ações baseadas apenas em intuição.


