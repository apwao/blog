from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
simple = SimpleMDE()

mail = Mail()

login_manager = LoginManager()


login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    mail.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)
    
    from .user import user
    app.register_blueprint(user)

    from .requests import configure_request
    configure_request(app)

    return app

