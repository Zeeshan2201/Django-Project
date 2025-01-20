# Chat Application - Django Project

This is a simple chat application built using Django. Users can sign up, log in, and communicate with other users in real-time via a chat interface. The application uses WebSockets for real-time messaging and stores all user data and chat messages in a database.

## Features
- **User Sign Up**: New users can sign up with a username and password.
- **User Login**: Registered users can log in to the application.
- **Real-time Chat**: Users can send and receive messages in real-time.
- **User List**: All registered users are shown in a collapsible menu.
- **Chat History**: Previous messages between users are displayed when chatting.

## Technologies Used
- Python 3.x
- Django 5.x
- WebSockets (for real-time messaging)
- SQLite (Database)

## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Django 5.x

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/chatapp.git
cd chatapp
```

### Step 2: Create and Activate Virtual Environment
Create a virtual environment to manage the project's dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install Django and other dependencies like this:

```bash
pip install django channels
```

### Step 4: Set Up Database
Run the following commands to create the database and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)
If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Step 6: Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

The application will be running at `http://127.0.0.1:8000/`.

### Step 7: Access the Application
- Visit the login page: `http://127.0.0.1:8000/login/`
- Sign up a new user or log in with an existing one.

### Step 8: Access Admin Panel (Optional)
If you created a superuser, you can access the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials to manage users, messages, and other data.

## How to Use the Chat
1. **Sign up**: Click on the "Sign up" link on the login page.
2. **Log in**: After signing up, log in with your credentials.
3. **Chat**: Once logged in, you'll be directed to the chat room where you can see a list of registered users on the left side. Click on a user to start a chat.
4. **Send Messages**: Type your message in the input box and press send to chat with the selected user.

## Contributing
If you would like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a description of your changes.

## License
This project is licensed under the MIT License.

