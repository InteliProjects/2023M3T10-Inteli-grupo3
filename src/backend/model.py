import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def target(df):
    df_main = df.dropna(subset=["Patrimonio_Liquido"])
    inadimplentes = df_main["Carteira_Direitos_Aquisicao_Inadimplentes"]
    patrimonio_liquido = df_main["Patrimonio_Liquido"]
    taxa_inadimplencia = inadimplentes / patrimonio_liquido

    df_main = df_main.assign(taxa_inadimplencia_series=taxa_inadimplencia)

    return df_main

def cluster_and_return(df_main, carteira_nome):
    fundos = df_main[
        (df_main['taxa_inadimplencia_series'] != 0) &
        df_main['taxa_inadimplencia_series'].notna() &
        df_main[carteira_nome].notna() 
    ]

    X = fundos[[carteira_nome]]

    kmeans = KMeans(n_clusters=3)
    fundos['grupo'] = kmeans.fit_predict(X)

    cluster_results = []

    for grupo in range(3):
        grupo_df = fundos[fundos['grupo'] == grupo]
        cluster_result = {
            'carteira_nome': carteira_nome,
            'cluster_numero': grupo,
            'indices': grupo_df.index.tolist(),
            'valores': grupo_df[carteira_nome].tolist(),
        }
        cluster_results.append(cluster_result)

    cluster1 = fundos[fundos['grupo'] == 1]
    cluster1 = cluster1.sort_values(by='taxa_inadimplencia_series', ascending=False)
    fundos_inadimplencia = cluster1.head(10)

    inadimplencia_results = []

    for _, row in fundos_inadimplencia.iterrows():
        inadimplencia_result = {
            'Nome_Fundo': row["Nome_Fundo"],
            'CNPJ': row["CNPJ"],
            'Taxa_de_Inadimplencia': row["taxa_inadimplencia_series"],
            'Data_de_Competencia': row["Data_Competencia"],
        }
        inadimplencia_results.append(inadimplencia_result)

    return cluster_results, inadimplencia_results

df = read_csv("IM_230626_semNP.csv")

df_main = target(df)

carteira_financeiro = 'Carteira_Financeiro'
cluster_results, inadimplencia_results = cluster_and_return(df_main, carteira_financeiro)

if __name__ == "__main__":
    print(cluster_results)

