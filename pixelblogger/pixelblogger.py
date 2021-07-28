from flask_migrate import Migrate
from sassutils.wsgi import SassMiddleware
from sassutils.builder import Manifest
from app import create_app, db
from app.models import User, Role

import os


manifest = Manifest(sass_path='static/scss', css_path='static/css', wsgi_path='/static/css', strip_extension=True)
app = create_app(os.getenv('FLASK_CONFIG', 'default'))
migrate = Migrate(app, db)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
  'app': manifest
})

@app.shell_context_processor
def make_shell_context():
  return dict(db=db, User=User, Role=Role)