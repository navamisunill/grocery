# Load environment variables from the .env file
from dotenv import load_dotenv 
# from python-dotenv import load_dotenv
load_dotenv()

# Import required modules
import os
from flask_sqlalchemy import SQLAlchemy
from app import app

# Configure the Flask application using environment variables
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 

# You can access these configuration values throughout your Flask application
import models