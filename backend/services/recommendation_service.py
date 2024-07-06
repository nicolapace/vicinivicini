from models.recommendation_model import RecommendationModel
from services.data_service import DataService

class RecommendationService:
    def __init__(self):
        self.model = RecommendationModel()
        self.data_service = DataService()
        self._train_model()

    def _train_model(self):
        items_df = self.data_service.load_data()
        self.model.train(items_df)

    def get_recommendations(self, user_preferences):
        # This is a simplified version. In a real app, you'd need to match
        # user_preferences to items and then get recommendations based on those items.
        sample_item_index = 0
        return self.model.get_recommendations(sample_item_index)
