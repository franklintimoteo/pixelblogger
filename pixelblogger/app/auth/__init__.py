from flask import Blueprint
from ..forms import LoginForm

auth = Blueprint('auth', __name__)

from . import views