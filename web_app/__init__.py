from flask import Flask

from web_app.routes.home_routes import home_routes


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)