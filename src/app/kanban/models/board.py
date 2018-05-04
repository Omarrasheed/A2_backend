from . import *
import app

class Board(Base):
  __tablename__ = 'boards'
  id             = db.Column(db.Integer, primary_key=True)
  title          = db.Column(db.String(256), unique=True, nullable=False)
  elements       = db.relationship("Board_Element", backref="board")

  def __init__(self, **kwargs):
    """
    Constructor
    """
    self.title = kwargs.get('title', None)

class Board_Element(Base):
  __tablename__ = 'board_elements'
  id             = db.Column(db.Integer, primary_key=True)
  category       = db.Column(db.String(256), nullable = False)
  description    = db.Column(db.String(256), nullable = False)
  board_id       = db.Column(db.Integer, db.ForeignKey('boards.id'))

  def __init__(self, **kwargs):
    self.category = kwargs.get('category', None)
    self.description = kwargs.get('description', None)
    self.board_id = kwargs.get('board_id', None)
