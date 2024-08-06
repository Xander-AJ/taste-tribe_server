from app import create_app, db
from models import (
    User,
    Profile,
    Recipe,
    Ingredient,
    Comment,
    Rating,
    Bookmark,
    Follow,
    Notification,
)

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Profile": Profile,
        "Recipe": Recipe,
        "Ingredient": Ingredient,
        "Comment": Comment,
        "Rating": Rating,
        "Bookmark": Bookmark,
        "Follow": Follow,
        "Notification": Notification,
    }


if __name__ == "__main__":
    app.run()
