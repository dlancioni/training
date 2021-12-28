from flask import Flask
from db.config import db
from db.migrations import create_db
from bp.user import bp_user
from bp.category import bp_category

def setup_database(app):
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/test.db"
    db.init_app(app)
    
def setup_blueprints(app):
    app.register_blueprint(bp_user, url_prefix = "")
    app.register_blueprint(bp_category, url_prefix = "")

def create_app():
    app = Flask(__name__)
    setup_database(app)
    setup_blueprints(app)
    return app

if __name__ == "__main__":
    app = create_app()
    create_db(app, db)
    app.run()