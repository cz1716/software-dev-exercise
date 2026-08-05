from flask import Blueprint, request


home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
@home_routes.route("/home")
def home() -> str:
    """Display the home-page message."""
    return "Welcome Home"


@home_routes.route("/about")
def about() -> str:
    """Display the about-page message."""
    return "About Me"


@home_routes.route("/hello")
def hello() -> str:
    """Display a greeting using an optional URL parameter."""
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"