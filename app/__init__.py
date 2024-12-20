from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Register blueprints or initialize extensions here
        from .views import main_bp
        app.register_blueprint(main_bp)

        return app