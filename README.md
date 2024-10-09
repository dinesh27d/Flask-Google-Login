# Flask Google Login with Firebase Integration


Easily integrate Google OAuth and Firebase Authentication into your Flask web application by following this step-by-step guide. This project demonstrates a streamlined process for handling user authentication.


## 🚀 Features


- Google OAuth 2.0 for secure login.
- Firebase for backend user management.
- Seamless Flask integration for modern web apps.


## 🛠 Prerequisites


Ensure you have the following installed before setting up the project:


- Python 3.x
- Flask
- Firebase account and Google Cloud Console access
- A valid Google OAuth Client ID


---


## 🔑 Step 1: Set Up Google OAuth


1. Head over to [Google Cloud Console](https://console.cloud.google.com).
2. Navigate to **APIs and Services** -> **Credentials** and select **OAuth Client ID**.
3. Follow these steps to configure the OAuth consent screen:
   - Set the application name to `flask`.
   - Provide your email in **User Support Email** and **Developer Email** fields.
   - Click **Save and Continue**.


4. **Create OAuth Client ID**:
   - Go back to **Credentials**.
   - Edit your **OAuth Client ID**.
   - Add the authorized URL for redirecting your logins.


---


## 🔥 Step 2: Set Up Firebase


1. Visit [Firebase](https://firebase.google.com/) and click on **Get Started**.
2. Create a project and download the Firebase JSON configuration file.
   - **Important:** Keep this file safe as it contains sensitive credentials.


---


## 📁 Step 3: Set Up Your Flask Project


1. Create a new project directory.
2. Clone the repository from GitHub.


---


## 📦 Step 4: Install Dependencies


Navigate to your project directory and install the required dependencies.


---


## ⚙️ Step 5: Configure Flask Application


1. Open `app.py` in your IDE and modify the following:
   - Update paths for the Google OAuth console and Firebase JSON configuration.
   - Enter your `google_client_id`, `google_client_secret`, and any other required values from the JSON.


---


## ▶️ Step 6: Run the Flask Application


Once you've configured your application:


1. Navigate to the folder containing `app.py`.
2. Run the application.
3. Visit `http://localhost:5000` in your browser and test the Google login integration.


---


## 📝 Notes


- **OAuth 2.0:** Ensure your redirect URIs are correctly configured in the Google Cloud Console.
- **Firebase JSON:** Keep your Firebase credentials secure and out of version control.


---






Happy coding! 😊
