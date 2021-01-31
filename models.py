from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

default_image = ' https://tinyurl.com/demo-cupcake0'


class Cupcake(db.Model):
    """Cup cake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_image)


    def serialize(self):
        """Returns a dict representation of cup cake which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    def __repr__(self):
        return f"<Cup cake {self.flavor} size={self.size} rating={self.self.rating} >"
