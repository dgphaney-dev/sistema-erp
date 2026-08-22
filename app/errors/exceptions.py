class ERPException(Exception):
    """Exceção base para doto o ERP de materiais de construção"""
    def __init__(self, message, error_code="SYS_500", status_code=500, details=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details or {}

class UsuarioNaoEncontradoError(ERPException):
    def __init__(self, usuario_id):
        super().__init__(
            message=f"O usuário com ID {usuario_id} não foi encontrado.",
            error_code="USER_404",
            status_code=404,
            details={"usuario_id": usuario_id}
        )