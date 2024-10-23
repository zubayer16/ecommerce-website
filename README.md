# E-Commerce Website

This project is a fully functional e-commerce website built using Django. This guide provides instructions to set up and run the project locally.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.12** (or compatible version)
- **pip** (Python package installer)
- **virtualenv** (optional but recommended)
- **Git**

## Setup Instructions

### 1. Install Required Software

Verify that Python and pip are installed by running:

```bash
python --version
pip --version
```
2. Install virtualenv (Optional but Recommended)
Using a virtual environment is optional but highly recommended to avoid dependency issues.

Install virtualenv using pip:

```bash
pip install virtualenv
```
3. Clone the Project Repository

```bash
git clone https://github.com/zubayer16/ecommerce-website.git
cd ecommerce-website
```
4. Set Up a Virtual Environment

Create a virtual environment inside the project folder:

```bash
python -m venv env
```

Activate the virtual environment:

For Windows:

```bash
.\env\Scripts\activate
```
For macOS/Linux:

```bash
source env/bin/activate
```
5. Install Project Dependencies

Install the required Python packages listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
6. Migrate the Database

Run the following command to apply migrations and set up the database:

```bash
python manage.py migrate
```
7. Create a Superuser (Optional)
   
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin user.

8. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
9. Access the Application
Open your web browser and navigate to:

Main application: http://127.0.0.1:8000/
Admin panel (if superuser created): http://127.0.0.1:8000/admin/
Troubleshooting
Common Issues:
Missing or outdated packages: If you encounter issues related to missing packages (like Pillow), try the following:

Re-install Pillow:

```bash
pip install pillow
```
Upgrade pip:

```bash
python -m pip install --upgrade pip
```
Upgrade setuptools and wheel:

```bash
python -m pip install --upgrade setuptools wheel
```
Issues with Python or Django versions: Ensure that you're using the correct version of Python and Django as specified in the requirements.txt.
