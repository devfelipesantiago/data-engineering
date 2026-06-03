# 📊 Mini Projeto: Análise de Faturamento de E-commerce

## 📖 Sobre o Projeto
Este projeto tem como objetivo realizar a análise de dados de vendas de uma loja de e-commerce em fase de crescimento. O foco principal é transformar dados brutos de transações diárias em insights acionáveis, auxiliando a equipe gestora na tomada de decisões estratégicas em áreas como gestão de estoque, marketing e expansão.

## 🎯 Problema de Negócio e Objetivos
As decisões de negócio eram baseadas em intuição, gerando problemas de estoque, campanhas genéricas e perda de oportunidades. O projeto busca responder a quatro perguntas fundamentais:
- **O que vender?** Identificar os produtos de maior sucesso para otimizar o portfólio.
- **Onde focar?** Compreender as categorias que geram a maior receita.
- **Quando agir?** Analisar a evolução do faturamento mensal, tendências e sazonalidades.
- **Para onde expandir?** Mapear a distribuição geográfica das vendas.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Manipulação de Dados:** `pandas`, `numpy`
- **Visualização de Dados:** `matplotlib`, `seaborn`
- **Outras bibliotecas:** `datetime`, `random`

## 🚀 Estrutura e Etapas do Projeto
1. **Geração de Dados:** Criação de uma base de dados realista (fictícia) utilizando funções em Python, simulando vendas (eletrônicos, móveis, hardware e acessórios).
2. **Pré-processamento e Engenharia de Atributos:**
   - Limpeza e conversão de tipos de dados (datas).
   - Criação da feature `Faturamento` (Preço Unitário × Quantidade).
   - Criação da feature `Status_Entrega` com base no estado de destino.
3. **Análise Exploratória de Dados (EDA) e Visualizações:**
   - **Análise 1:** Top 10 Produtos Mais Vendidos (Gráficos de barras).
   - **Análise 2:** Evolução do Faturamento Mensal (Gráficos de linhas marcadas).
   - **Análise 3:** Faturamento por Estado (Gráficos de barras verticais e paletas customizadas).
   - **Análise 4:** Faturamento por Categoria (Formatação customizada de eixos com valores em milhares - K).

## 📈 Benefícios e Impacto no Negócio
Ao aplicar conceitos de Data Science neste conjunto de dados, foi possível entregar:
- **Otimização de Estoque:** Ajuste de compras com base nos top 10 produtos e identificação do que fica parado nas prateleiras.
- **Marketing Segmentado:** Campanhas direcionadas aos estados e categorias com maior retorno financeiro.
- **Previsibilidade:** Planejamento financeiro aprimorado devido ao mapeamento do faturamento ao longo dos meses.
- **Cultura Data-Driven:** Substituição do "achismo" por decisões orientadas a dados reais.

## 💻 Como Executar
1. Certifique-se de ter o Python (3.x) instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Execute o script (ou abra-o em um ambiente Jupyter caso queira visualizar os gráficos célula a célula):
   ```bash
   python Mini_Projeto_Faturamento.py
   ```

---
*Projeto de portfólio focado em Data Science, Análise de Dados e Inteligência de Negócios.*
