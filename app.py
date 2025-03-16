from flask import Flask

from extentions import bcrypt
from routes.test_routes import test_bp
from extentions import db
from routes.users_routes import users_bp

app = Flask(__name__)

app.config.from_object('config.Config')

# @app.route('/')
# def home():
#     return f"Debug: {app.config['DEBUG']}, Secret: {app.config['SECRET_KEY']}"

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(test_bp, url_prefix='/test')

if __name__ == '__main__':
    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
