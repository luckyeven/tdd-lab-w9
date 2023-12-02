# manage.py
import sys
from flask.cli import FlaskGroup
from src import create_app, db  # new
from src.api.models import User  # new
app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='john', email="john@algonquincollege.com"))
    db.session.add(User(username='Dave', email="dave@algonquincollege.com"))
    db.session.commit()
if __name__ == '__main__':
    cli()
