# Clusterização de Empresas com K-Means e PCA

Este projeto realiza a clusterização de empresas com o algoritmo K-Means e aplica Análise de Componentes Principais (PCA) para visualização dos clusters em 2D. Os dados são carregados de um arquivo Excel e processados para gerar insights sobre a classificação das empresas.

## 📌 Funcionalidades
- Carregamento de dados de um arquivo Excel
- Pré-processamento e padronização dos dados
- Aplicação do algoritmo de clusterização K-Means com 4 clusters
- Mapeamento dos clusters para categorias específicas (Ouro, Prata, Diamante e Bronze)
- Redução de dimensionalidade com PCA para visualização 2D
- Plotagem dos clusters com indicação de variáveis relevantes
- Exportação dos resultados para um novo arquivo Excel

## 📂 Estrutura do Código
1. **Carregamento dos Dados**: O arquivo Excel é lido e processado.
2. **Pré-processamento**: As colunas numéricas são padronizadas com `StandardScaler`.
3. **Clusterização**: O K-Means é aplicado para identificar grupos de empresas.
4. **Mapeamento dos Clusters**: Os clusters numéricos são convertidos em categorias nomeadas.
5. **Redução de Dimensionalidade**: O PCA reduz as dimensões para 2 componentes principais.
6. **Visualização**: O gráfico 2D é gerado com as empresas classificadas por cores.
7. **Exportação**: O DataFrame final é salvo em um novo arquivo Excel.

## 🚀 Tecnologias Utilizadas
- Python
- Pandas
- NumPy
- Scikit-Learn (K-Means, StandardScaler, PCA)
- Matplotlib

## 🔧 Como Utilizar
1. **Baixe ou clone este repositório**
2. **Instale as dependências necessárias:**
   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```
3. **Modifique o caminho do arquivo de entrada no código** para apontar para seu arquivo Excel.
4. **Execute o script**
   ```bash
   python script.py
   ```
5. **Verifique a saída:**
   - O gráfico 2D será exibido.
   - O arquivo Excel de saída conterá os clusters e componentes principais.

## 📊 Exemplo de Saída
O gráfico gerado exibe a distribuição das empresas em 2D com base nos componentes principais do PCA. As setas indicam a influência das variáveis no espaço reduzido.

## 📄 Licença
Este projeto é distribuído sob a licença MIT.


