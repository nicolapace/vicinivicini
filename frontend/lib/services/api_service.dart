import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  final String baseUrl = 'http://localhost:5000/api';

  Future<List<String>> getRecommendations(List<String> userPreferences) async {
    final response = await http.post(
      Uri.parse('$baseUrl/recommendations'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'preferences': userPreferences}),
    );

    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      return data.map((item) => item.toString()).toList();
    } else {
      throw Exception('Failed to load recommendations');
    }
  }
}
