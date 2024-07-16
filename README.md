# Flask-Google-Login

# Setting Up Google OAuth and Firebase for Flask Application

## Step 1: Set Up Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com).
2. Navigate to **APIs and Services** -> **Credentials**.
3. Select **OAuth client ID**.

#### Create OAuth Consent Screen

4. Enter `flask` as the name and provide your email address in both **User Support Email** and **Developer Email**.
5. Click **Save and Continue**.

#### Edit OAuth Client ID

6. Go back to **Credentials**.
7. Edit your **OAuth client ID**.
8. Add the authorized URL to redirect your logins through.

## Step 2: Set Up Firebase

1. Go to [Firebase](https://firebase.google.com/) and click on **Get Started**.
2. Enter all the required information.
3. Download the JSON file provided by Firebase.

## Step 3: Create a New Folder for Your Flask Application

1. Create a new folder and open it in any IDE:

		mkdir flask-google-login
		cd flask-google-login

3. Clone the repository:

		git clone https://github.com/dinesh27d/Flask-Google-Login.git

## Step 4: Install The Requirements file

	 pip install -r requirements.txt

## Step 5: Configure Your Flask Application

1. Edit your paths for the console and Firebase JSON file in the app.py.
2. Enter your google_client_id and other required details from the JSON file.

## Step 6: Run Your Flask Application

1. Navigate to the directory containing app.py.
2. Run the application:

		python app.py

