from flask import render_template_string
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template_string('Página não encontrada error handler'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template_string("Erro interno error handler"), 500