# Setting Up and Running the Recommendation App Demo

## Backend Setup (Python)

1. Set up a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install required Python packages:
   ```
   pip install flask pandas scikit-learn
   ```

3. Create the project structure:
   ```
   mkdir -p backend/models backend/services backend/utils backend/datasets
   ```

4. Create and populate the Python files as shown in the previous code samples.

5. Add sample data:
   Create CSV files in `backend/datasets/` for books, movies, and games. Each file should have at least 'title' and 'description' columns.

6. Run the Flask app:
   ```
   python backend/app.py
   ```
   The backend should now be running on `http://127.0.0.1:5000`.

## Frontend Setup (Flutter)

1. Install Flutter if you haven't already: https://flutter.dev/docs/get-started/install

2. Create a new Flutter project:
   ```
   flutter create frontend
   cd frontend
   ```

3. Update `pubspec.yaml` to include the http package:
   ```yaml
   dependencies:
     flutter:
       sdk: flutter
     http: ^0.13.3
   ```

4. Run `flutter pub get` to install dependencies.

5. Replace the contents of `lib/main.dart` and create other Dart files as shown in the previous code samples.

6. Update `lib/services/api_service.dart` to use the correct backend URL:
   ```dart
   final String baseUrl = 'http://10.0.2.2:5000/api';  // For Android emulator
   // Use 'http://localhost:5000/api' for iOS simulator or web
   ```

7. Run the Flutter app:
   ```
   flutter run
   ```

## Running the Demo

1. Ensure the backend Flask app is running.
2. Run the Flutter app on an emulator, simulator, or physical device.
3. On the home screen, tap "Get Recommendations".
4. You should see a list of recommended items based on the sample data.

## Troubleshooting

- If you encounter CORS issues, install the `flask-cors` package in the backend and update `app.py`:
  ```python
  from flask_cors import CORS
  app = Flask(__name__)
  CORS(app)
  ```

- For network issues on Android emulator, ensure you're using `10.0.2.2` instead of `localhost` in the API URL.

- For iOS, you may need to add permissions to `Info.plist`:
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
  </dict>
  ```