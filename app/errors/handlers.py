from flask import jsonify
from app.errors.exceptions import ERPException

def register_error_handlers(app):
    """Registra os tratadores de erro globais da aplicação"""
    @app.errorhandler(ERPException)
    def handle_erp_exception(error):
        response = {
            "success": False,
            "error": {
                "code": error.error_code,
                "message": error.message,
                "details": error.details
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": {
                "code": "SYS_404",
                "message": "Recurso nao encontrado."
            }
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "success": False,
            "error": {
                "code": "SYS_500",
                "message": "Erro interno no servidor."
            }
        }), 500