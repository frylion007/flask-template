from flask import Flask
from api.controllers import api_bp
from admin.controllers import admin_bp

app = Flask(__name__)

app.config.from_object('config.config')

app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
