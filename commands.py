from application import application
from extensions.database import db


@application.cli.command()
def create_database():
    from extensions.database import db

    db.create_all()
