from flask_migrate import Migrate
from app.models import db
migrate = Migrate()

def init_app(app):
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)