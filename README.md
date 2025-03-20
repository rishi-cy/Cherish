# Travel Chronicle

A Progressive Web App for tracking and sharing travel experiences.

## Features

- User authentication
- Interactive map with location marking
- Image upload support
- Offline functionality
- Mobile-friendly interface
- Installable on Android and iOS devices

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your secret key:
   ```
   SECRET_KEY=your_secure_secret_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Deployment

This application is configured for deployment on Render.com:

1. Create a Render account at https://render.com
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Environment Variables:
     - `SECRET_KEY`: Your secure secret key
     - `PYTHON_VERSION`: 3.9.0

## Mobile Installation

### Android
1. Open the website in Chrome
2. Click "Add to Home Screen"
3. Follow the installation prompts

### iOS
1. Open the website in Safari
2. Tap the share button
3. Select "Add to Home Screen"
4. Tap "Add"

## Security Notes

- The application uses secure password hashing
- File uploads are validated and sanitized
- HTTPS is enforced in production
- Session management is implemented 