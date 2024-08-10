from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .profile import Profile
from .recipe import Recipe
from .comment import Comment
from .rating import Rating
from .bookmark import Bookmark
from .follow import Follow
from .notification import Notification
