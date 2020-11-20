import os
from flask import Flask, request, render_template, render_template_string,session,url_for,jsonify,make_response
from werkzeug.utils import secure_filename
import numpy as np
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import sql
from json import dumps
from flask_mail import Mail,Message
import json

