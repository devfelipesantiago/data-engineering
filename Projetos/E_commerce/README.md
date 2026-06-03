# 🛒 Mini Projeto: Análise e Limpeza de Dados de E-commerce

## 📖 Sobre o Projeto
Este projeto simula um cenário muito comum na área de dados: a necessidade de extrair inteligência de negócio a partir de **dados transacionais brutos e corrompidos**. 

O foco central aqui não é apenas construir gráficos, mas demonstrar domínio em etapas críticas de **Limpeza de Dados (Data Cleaning)** e **Pré-processamento**. Tratar os dados de forma correta é o primeiro e mais importante passo para garantir que a liderança tome decisões baseadas em informações confiáveis.

## 🎯 O Problema de Negócio
A empresa de e-commerce enfrentava sérias dificuldades para analisar seu desempenho. Seus relatórios geravam métricas conflitantes devido à péssima qualidade dos dados do sistema, que apresentavam:
- **Valores Ausentes (NaN):** Campos importantes em branco.
- **Registros Duplicados:** Superestimando receitas e volumes.
- **Inconsistências de Tipagem:** Preços e IDs numéricos cadastrados como texto ou misturados com strings.
- **Valores Anômalos (Outliers):** Quantidades irreais distorcendo médias.

**Objetivo Estratégico:** Higienizar o banco de dados e entregar respostas precisas sobre:
1. Qual o faturamento real e a receita por categoria?
2. Quais os produtos "campeões" de venda?
3. Qual a tendência temporal de vendas (sazonalidade diária)?
4. Como está distribuída a eficiência logística (status de entrega)?

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Estruturação e Limpeza:** `pandas`, `numpy`
- **Visualização Estática:** `matplotlib`, `seaborn`
- **Visualização Interativa Avançada:** `plotly`

## 🚀 Etapas do Projeto
1. **Geração de Dados Corrompidos:** Criação de um banco de dados sintético injetando intencionalmente as falhas mencionadas para simular um ambiente caótico real.
2. **Data Cleaning (Higienização):**
   - Correção de *dtypes* (uso de `to_numeric` com `errors='coerce'`).
   - Imputação inteligente de dados nulos (mediana para quantidades para evitar impacto de outliers, e moda para atributos categóricos).
   - Identificação e remoção de duplicatas absolutas.
   - Tratamento de outliers utilizando a regra dos 3 desvios padrão.
3. **Feature Engineering:** Criação da variável alvo analítica `Total_Venda`.
4. **Análise Exploratória (EDA):** Extração dos KPIs de negócio através de agrupamentos e manipulação de séries temporais (`resample`).
5. **Geração de Insights Visuais:**
   - Gráficos de barras horizontais e verticais.
   - Tendência em gráfico de linhas para acompanhamento financeiro diário.
   - Diferentes abordagens de gráficos de composição (pizza clássica, 3D com sombra e uma solução **interativa do tipo Donut** construída com Plotly).

## 📈 Impacto Analítico
Ao implementar esta esteira de limpeza e análise, a empresa se capacita a:
- **Ter Confiança Financeira:** Relatórios imunes a duplicatas e erros de digitação.
- **Otimizar Logística:** Entender exatamente a porcentagem de falhas/pendências.
- **Agir com Precisão:** Direcionar campanhas de marketing com base em tendências limpas e verdadeiras.

## 💻 Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as bibliotecas requeridas:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
3. Rode o script (ou importe o código num Jupyter Notebook para interagir com o Plotly e visualizar cada passo do Data Cleaning):
   ```bash
   python Mini_Projeto_E-Commerce.py
   ```

---
