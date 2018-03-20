from flask import Blueprint
from views import LoginView

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

admin_bp.add_url_rule("/<user_name>/", view_func=LoginView, methods=["GET", "POST"])
