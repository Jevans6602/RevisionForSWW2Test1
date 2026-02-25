from app import db
import sqlalchemy.orm as so
import sqlalchemy as sa

class Game(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(256), unique=True)
    genre: so.Mapped[str] = so.mapped_column(sa.String(256))
    rating: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)

