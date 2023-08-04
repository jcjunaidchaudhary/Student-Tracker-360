from app import create_app, db
from app.md.models.user import User

app = create_app()  

@app.cli.command()
def load():
    """
    Drop, recreate, and load test data into database for development purposes.
    """

    default_user = User()
    default_user.id = -1
    default_user.name = "System"
    default_user.email = "system@leewayzon.com"
    default_user.password = "system"
    default_user.phone1 = 9702737441
    default_user.modified_user_id = -1

    db.session.add(default_user)

    db.session.commit()


if __name__ == "__main__":
    load()
