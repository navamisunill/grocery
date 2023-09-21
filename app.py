from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
#debug = True
app = Flask(__name__)

import config
#import models
#import routes
