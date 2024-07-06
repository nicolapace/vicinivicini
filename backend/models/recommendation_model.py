from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class RecommendationModel:
    def __init__(self):
        self.items_df = None
        self.tfidf_matrix = None

    def train(self, items_df):
        self.items_df = items_df
        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.items_df['description'])

    def get_recommendations(self, item_index, num_recommendations=5):
        cosine_sim = cosine_similarity(self.tfidf_matrix[item_index], self.tfidf_matrix)
        sim_scores = list(enumerate(cosine_sim[0]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        item_indices = [i[0] for i in sim_scores]
        return self.items_df['title'].iloc[item_indices].tolist()