from flask import Blueprint

wallets_bp = Blueprint('wallets', __name__)

@wallets_bp.route("/")
def wallets():
    return {
        "message": "Wallets route is running!"
    }, 200