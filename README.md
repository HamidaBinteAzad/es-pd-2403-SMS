
# Django Student Management System (SMS)

This is a Django-based **Student Management System (SMS)** project. It allows you to manage student data with features such as adding, editing, and deleting student records.

## Table of Contents
- [Clone the Repository](#clone-the-repository)
- [Setup Local Development Environment](#setup-local-development-environment)
  - [Create Virtual Environment](#create-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Database Migrations](#database-migrations)
- [Run the Application Locally](#run-the-application-locally)
- [Additional Notes](#additional-notes)

## Clone the Repository
To get started with this project, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## Setup Local Development Environment

### Create Virtual Environment
It's recommended to use a virtual environment to manage your project dependencies.

1. Navigate to the project folder:
   ```bash
   cd your-project-folder
   ```

2. Create a virtual environment named `env`:
   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```

   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

### Install Dependencies
With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Database Migrations
Once the dependencies are installed, you need to apply database migrations to set up your database.

1. Make migrations:
   ```bash
   python manage.py makemigrations
   ```

2. Apply migrations to the database:
   ```bash
   python manage.py migrate
   ```

## Run the Application Locally
After setting up the environment and applying migrations, you can run the Django development server locally:

```bash
python manage.py runserver
```

Visit the application at `http://127.0.0.1:8000/` in your web browser.

## Additional Notes
- Ensure you have Python 3.x installed on your system.
- The `requirements.txt` file contains all the necessary dependencies for the project.
- If you encounter any issues, please check the error messages in the terminal and refer to the [Django documentation](https://docs.djangoproject.com/).
