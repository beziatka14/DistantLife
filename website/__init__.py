from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='../static')

    from .views import views
    app.register_blueprint(views)

    return app
