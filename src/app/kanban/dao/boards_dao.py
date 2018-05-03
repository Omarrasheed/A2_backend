from app.constants import *
from . import *
#from app.kanban.models.board import Board
#import app.models
#from app import db

"""
Add more methods below!!!
"""

def board_by_id(board_id):
  """
  Get board by ID
  """
  return Board.query.filter_by(id=board_id).first()

def board_by_title(board_title):
	return Board.query.filter_by(title=board_title).first()

def all_boards():
	return Board.query.all()

def get_all_todo(idnum):
	return Board_elements.query.filter_by(category="todo", board_id=idnum).count()

def get_all_in_progress(board_id):
	return Board_elements.query.filter_by(category="inprogress",board_id=idnum).count()

def get_all_done(board_id):
	return Board_elements.query.filter_by(category="done", board_id=idnum).count()

def delete_board(board):
	db.session.delete(board)
	try:
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		return e

def create_board(board_title):
	firstboard = Board(title=board_title)
	db.session.add(firstboard)
	try:
		db.session.commit()
		return firstboard
	except Exception as e:
		db.session.rollback()
		return e
	
