from flask import Blueprint
from views import TestApiView

api_bp = Blueprint("api", __name__, url_prefix="/api")

api_bp.add_url_rule("/<user_name>/", view_func=TestApiView, methods=["GET", "POST"])
