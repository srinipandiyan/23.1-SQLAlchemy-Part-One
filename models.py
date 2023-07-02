"""SQLA Models for Blogly app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
default_profile_url = "https://images.unsplash.com/photo-1563089145-599997674d42?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    first_name = db.Column(db.String(20), 
                           nullable=False)
    last_name = db.Column(db.String(20), 
                          nullable=False)
    image_url = db.Column(db.String(250), 
                          nullable=False, 
                          default=default_profile_url)

    def __repr__ (self):
        """Show info about user"""
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', image_url='{self.image_url}')>"
    
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)