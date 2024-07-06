import 'package:flutter/material.dart';
import 'package:frontend/screens/recommendations_screen.dart';
import 'package:frontend/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  final ApiService _apiService = ApiService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home')),
      body: Center(
        child: ElevatedButton(
          child: Text('Get Recommendations'),
          onPressed: () async {
            List<String> recommendations =
                await _apiService.getRecommendations(['fantasy', 'sci-fi']);
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) =>
                      RecommendationsScreen(recommendations: recommendations)),
            );
          },
        ),
      ),
    );
  }
}
