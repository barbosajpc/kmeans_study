import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Carregar os dados do arquivo Excel com a primeira linha como cabeçalhos
path = r"insert here your path"
data = pd.read_excel(path)

# Selecionar a primeira coluna como nomes das empresas
company_names = data.iloc[:, 0]

# Selecionar colunas numéricas para o clustering (colunas B até J)
X = data.iloc[:, 1:10]

# Certificar que todos os nomes das colunas são strings
X.columns = X.columns.astype(str)

# Escalar os dados, ignorando NaN
X_scaled = StandardScaler().fit_transform(X)  # Preencher NaN com a média, por exemplo

# Inicializar e ajustar o KMeans com 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# Adicionar os rótulos dos clusters ao DataFrame
data['cluster'] = kmeans.labels_

# Mapeamento dos clusters numéricos para letras
cluster_mapping = {1: 'Prata', 0: 'Ouro', 2: 'Diamante', 3: 'Bronze'}
data['cluster'] = data['cluster'].map(cluster_mapping)

# Aplicar PCA para reduzir a dimensionalidade para 2 componentes
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Obter os loadings das variáveis
loadings = pca.components_.T

# Criar um DataFrame com os componentes principais e nomes das empresas
pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
pca_df['company'] = company_names.reset_index(drop=True)  # Adicionar nomes das empresas
pca_df['cluster'] = data['cluster'].reset_index(drop=True)

# Garantir que não haja valores NaN na coluna de cluster
pca_df = pca_df.dropna(subset=['cluster'])

# Definir uma paleta de cores personalizada para os clusters baseada nas classificações
color_mapping = {
    'Prata': '#C0C0C0',  # Cor prata
    'Ouro': '#FFD700',    # Cor ouro
    'Diamante': '#00FFFF',  # Cor diamante (azul claro como o brilho de diamante)
    'Bronze': '#CD7F32'   # Cor bronze
}
pca_df['color'] = pca_df['cluster'].map(color_mapping)

# Plotagem 2D
plt.figure(figsize=(12, 10))

# Plotar os dados no gráfico 2D com as cores dos clusters
scatter = plt.scatter(pca_df['PC1'], pca_df['PC2'], c=pca_df['color'], s=100, edgecolor='k')

# Adicionar os nomes das empresas no gráfico com uma fonte menor
for _, row in pca_df.iterrows():
    plt.text(row['PC1'], row['PC2'], row['company'], size=6, zorder=1, color='black')  # Fonte reduzida

# Desenhar os vetores de orientação (loadings) das 9 variáveis no gráfico 2D
for i, var in enumerate(X.columns):  # Nome das variáveis corretamente usando os cabeçalhos
    # Desenhar as setas (vetores dos loadings)
    plt.arrow(0, 0, loadings[i, 0]*4, loadings[i, 1]*4, 
              color='r', alpha=0.8, linewidth=1, head_width=0.1, head_length=0.1)  # Aumenta o comprimento, diminui a grossura
    
    # Posicionar e adicionar os rótulos das variáveis perto das setas
    plt.text(loadings[i, 0] * 3.75, loadings[i, 1] * 3.75, var, color='green', fontsize=6, weight='bold')

# Adicionar título e legendas dos eixos
plt.title('Clusters visualizados em 2D com PCA e Classificação das Empresas', fontsize=15)
plt.xlabel('PC1')
plt.ylabel('PC2')

# Adicionar uma legenda personalizada com as cores dos clusters
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_mapping[c], markersize=10, label=c)
           for c in cluster_mapping.values()]
plt.legend(handles=handles, title='Classificação', loc='best')

# Exibir o gráfico
plt.grid()
plt.show()

# Exportar o DataFrame PCA e clusters para um arquivo Excel
output_path = r"C:\Users\Cleane\OneDrive - AGENCIA DE ATRACAO INVESTIMENTOS ESTRATEGICO PIAUI\Área de Trabalho\aplications\kmeans\data_cluster_PCA_output_2D.xlsx"
pca_df.to_excel(output_path, index=False)
print(f"Arquivo PCA salvo em {output_path}")
