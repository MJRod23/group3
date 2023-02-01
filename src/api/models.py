from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#CREATE YOUR DATABASE TABLES HERE
class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }


class Recipe(db.Model):
    __tablename__ = "recipe"
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    api_id = db.Column(db.Integer, nullable=False, unique=True)
    carbs = db.Column(db.String(250), nullable=False)
    fat = db.Column(db.String(250), nullable=False)
    protein = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    calories = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    user=db.relationship("User")


    def __repr__(self):
        return f'<Recipe {self.user_id}>'

    def serialize(self):
        return {
            "user_id": self.user_id,
            "api_id": self.api_id,
            "fat": self.fat,
            "protein": self.protein,
            "title": self.title,
            "calories": self.calories,
            "image": self.image,
            "carbs": self.carbs,

            # do not serialize the password, its a security breach
        }