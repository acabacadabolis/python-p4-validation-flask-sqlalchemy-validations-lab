from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name doesnt exit')
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if not len(phone_number)==10:
            raise ValueError('Not valid Phone Number')
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError('Content too short')
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 249:
            raise ValueError('Summary too long')
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if not (category == 'Fiction' or category == 'Non-Fiction'):
            raise ValueError('Invalid category')
        return category
    
    @validates('title')
    def clickbait_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(bait in title for bait in clickbait):
            raise ValueError('Need clickbait title')
        return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
