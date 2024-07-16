from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
import os
import uuid
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Increase secret key length for security

# Initialize Firebase Admin SDK
cred = credentials.Certificate(" ") # Put the firebase json file path which was downloaded from firebase
firebase_admin.initialize_app(cred)

# OAuth configuration
oauth = OAuth(app)
GOOGLE_CLIENT_ID = '' # Add client Id from google developer console
GOOGLE_CLIENT_SECRET = '' # Add client secret from google developer console
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


# Routes
@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)


@app.route('/google/')
def google():
    # Check if the user is already logged in
    if 'user' in session:
        return redirect(url_for('profile'))

    # Generate a nonce
    nonce = str(uuid.uuid4())
    session['nonce'] = nonce

    # Update the redirect_uri to match your endpoint
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)


@app.route('/google/auth/')
def google_auth():
    try:
        # Authorize access token
        token = oauth.google.authorize_access_token()

        # Validate nonce to prevent CSRF
        nonce = session.pop('nonce', None)
        if not nonce:
            return 'Error: No nonce found in session.'

        # Parse ID token to get user information
        user = oauth.google.parse_id_token(token, nonce=nonce)
        session['user'] = user
        print("Google User:", user)

        # Check if user exists in Firebase Authentication
        try:
            firebase_user = auth.get_user_by_email(user['email'])
            print("Firebase User already exists:", firebase_user.uid)
        except auth.UserNotFoundError:
            # Create new user in Firebase Authentication
            firebase_user = auth.create_user(email=user['email'])
            print("Created new Firebase User:", firebase_user.uid)

        print("Firebase User UID:", firebase_user.uid)

    except Exception as e:
        print("Error during authentication:", e)
        return redirect('/')

    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect('/')
    return render_template('profile.html', user=user)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')