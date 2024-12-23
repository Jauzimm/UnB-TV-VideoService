import pandas as pd
import pickle
import os

# Obtém uma lista de vídeos recomendados a partir de um ID
def get_recommendations(id):

    cosine_path = '/app/src/recommendation_model/cosine_similarity.pkl'
    # Teste para garantir que o arquivo está acessível
    if not os.path.exists(cosine_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {cosine_path}")
    
    print("Conteúdo do diretório recommendation_model:", os.listdir('/app/src/recommendation_model'))

    with open('/app/src/recommendation_model/cosine_similarity.pkl', 'rb') as f:
        cosine_sim = pickle.load(f)

    df = pd.read_csv('/app/src/recommendation_model/df_videos.csv')

    indices = pd.Series(df.index, index=df['ID']).drop_duplicates()

    if id not in indices:
        return []

    try:
        sim_scores = sorted(list(enumerate(cosine_sim[indices[id]])), key=lambda x: x[1], reverse=True)[
                 1:8]  # Pega os 7 melhores
        video_indices = [i[0] for i in sim_scores]
        return list(df.iloc[video_indices][['ID']]['ID'])
    except:
        return []