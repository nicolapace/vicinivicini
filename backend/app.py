
from flask import Flask, request, jsonify
from services.recommendation_service import RecommendationService

app = Flask(__name__)
recommendation_service = RecommendationService()

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    user_preferences = data.get('preferences', [])
    recommendations = recommendation_service.get_recommendations(user_preferences)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)