# 🛒 Análise de Comportamento de Usuários de E-commerce (Mini Projeto de Marketing)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)

## 📌 Sobre o Projeto

Este projeto consiste em uma análise estatística exploratória voltada para o setor de marketing de um e-commerce. O objetivo principal é extrair insights a partir de dados simulados de navegação e compras dos usuários, a fim de identificar padrões de comportamento que impulsionam o faturamento e orientar estratégias de marketing mais assertivas.

O projeto foi desenvolvido em Python, focado principalmente na utilização intensiva da biblioteca **NumPy** para operações de arrays e estatística, juntamente com **Pandas**, **Matplotlib** e **Seaborn** para estruturação e visualização dos dados.

## 💼 Contexto e Problema de Negócio

Uma plataforma de e-commerce coleta grande volume de dados sobre a interação de seus usuários (visitas, duração da sessão, itens no carrinho e valor final). Porém, as decisões de marketing estavam sendo tomadas de forma genérica e sem base em dados comportamentais sólidos. 

**O desafio:** Compreender os padrões que diferenciam "Clientes de Alto Valor" de visitantes que apenas navegam e não compram, respondendo a perguntas críticas como:
1. Qual é o perfil médio do usuário?
2. Como se comportam os clientes de alto valor?
3. Onde está a oportunidade de conversão com os usuários que não compram?
4. Existe correlação estatística entre o tempo gasto no site, itens no carrinho e a compra final?

## 🛠️ Metodologia e Tecnologias

Para responder a essas perguntas, os dados foram gerados e analisados utilizando:
- **NumPy**: Geração de dados sintéticos (distribuição normal, aleatoriedade), manipulação de matrizes (`ndarrays`), e cálculo de métricas estatísticas (média, mediana, desvio padrão, correlação).
- **Pandas & Seaborn**: Criação de DataFrames para facilitar a plotagem de mapas de calor (Heatmaps) da matriz de correlação.
- **Matplotlib**: Geração de histogramas para visualizar a distribuição dos valores de compras.

## 📊 Principais Insights e Resultados

Através da análise de uma amostra de 500 usuários, descobrimos que:

* **Perfil Geral:** O usuário médio acessa a plataforma cerca de 26 vezes por mês, passa ~33 minutos logado, adiciona 7 itens ao carrinho e gasta **R$ 252,70**.
* **Segmentação de Alto Valor:** Clientes que gastam mais de R$ 250 (metade da base) apresentam forte engajamento: visitam o site com mais frequência (média de 33 visitas) e passam mais tempo navegando (37 minutos).
* **Oportunidades de Conversão (Visitantes sem Compra):** Os usuários que não finalizam compras visitam a página, em média, 7 vezes e ficam por quase 15 minutos. Representam uma oportunidade valiosa para campanhas de **remarketing** e otimização da experiência de checkout.
* **Correlações Relevantes:**
  * **Correlação Perfeita (1.00)** entre o número de itens no carrinho e o valor final da compra.
  * **Correlação Positiva (0.65)** entre a frequência de visitas e o valor da compra.
  * **Correlação Moderada (0.59)** entre o tempo no site e o valor da compra.

**Conclusão Estratégica:** O engajamento (tempo logado e frequência de acessos) tem forte peso na decisão de compra. Campanhas de marketing devem focar não apenas em conversão direta, mas em incentivar que o cliente explore o site por mais tempo e construa um carrinho de compras maior (ex: oferecendo descontos progressivos).

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado (recomendado 3.8+).
2. Instale as bibliotecas necessárias:
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```
3. Execute o script da análise:
   ```bash
   python Mini_Projeto_Marketing.py
   ```
