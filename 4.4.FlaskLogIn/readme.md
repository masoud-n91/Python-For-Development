# Chatbot Web Application

This is a web application for a chatbot developed using Python (Flask) as the backend and HTML, CSS, and JavaScript for the frontend. The application includes a login page with usernames and passwords stored in an SQL database.

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
  - [Using Flask](#using-flask)
  - [Using Docker](#using-docker)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/masoud-n91/Python-For-Development.git
   cd 4.4.FlaskLogIn
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File:**
   Create a `.env` file in the root directory of the project with the following content (replace the placeholder values with your actual credentials and keys):
   ```dotenv
   SECRET_KEY=your_secret_key
   MAIL_USERNAME=your_email@example.com
   MAIL_PASSWORD=your_email_password

   AUTH_HOST=your_auth_host
   AUTH_USER=your_auth_user
   AUTH_PASSWORD=your_auth_password
   AUTH_DATABASE=your_auth_database

   DATA_HOST=your_data_host
   DATA_USER=your_data_user
   DATA_PASSWORD=your_data_password
   DATA_DATABASE=your_data_database

   GOOGLE_API_KEY=your_google_api_key

   POSTGRES_PORT=your_postgres_port
   ```

## Running the Application

### Using Flask

To run the application locally:

1. **Run the Application:**
   ```bash
   flask run
   ```

2. **Run the Application in Debug Mode:**
   ```bash
   flask run --debug
   ```

### Using Docker

1. **Build the Docker Image:**
   ```bash
   docker build -t chatbot-app .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 chatbot-app
   ```

The application will be accessible at `http://localhost:5000`.

## Project Structure

```
├── static/
│   ├── css/
│   ├── js/
├── templates/
│   ├── index.html
│   └── other-html-files.html
├── .venv/
├── .gitignore
├── Dockerfile
├── requirements.txt
├── app.py
├── README.md
```

- `static/`: Static files (CSS, JS).
- `templates/`: HTML templates.
- `.venv/`: Virtual environment.
- `.gitignore`: Specifies files to ignore in the repository.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies.
- `app.py`: Entry point to run the application.
- `README.md`: This README file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

