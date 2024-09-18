import os
import subprocess

def run_django_server():
    # Navigate to the Django project directory
    os.chdir("Compare_My_Shop")

    # Run the Django server
    subprocess.run(['py', 'manage.py', 'runserver'])

if __name__ == "__main__":
    run_django_server()

