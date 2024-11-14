
# Djuix: Pre-bundled Django Project Setup Guide

This guide walks you through the process of setting up and running the pre-bundled Djuix Django project.

## Setup and Running

Now that you have your project, follow the setup instructions below:

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Locate the `.env` file in the project root.
   - Update the variables as needed for your setup.

8. Apply database migrations: 
   ```
   python manage.py migrate
   ```

9. Run the Django development server:
   ```
   python manage.py runserver
   ```

## Environment Variables

The `.env` file contains important configuration variables. Customize these as needed:

```
DEBUG=True
SECRET_KEY=your_secret_key_here
```

## Adding New Apps

To add a new app to your Djuix project:

1. Create a new app in the `apps/` directory:
   ```
   python manage.py startapp app_name apps/app_name
   ```

2. Add the app to `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'apps.app_name',
   ]
   ```

## Deployment

For deployment, ensure you set `DEBUG=False` and update other environment variables appropriately for production use. Follow Django's deployment guidelines for your specific hosting environment.

For more information, refer to the documentation included in the project files.

