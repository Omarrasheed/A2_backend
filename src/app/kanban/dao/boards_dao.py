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

def element_by_id(element_id):
	return Board_Element.query.filter_by(id=element_id).first()

def board_by_title(board_title):
	return Board.query.filter_by(title=board_title).first()

def all_boards():
	return Board.query.all()

def get_todo_list(idnum):
	returnList = []
	query = Board_Element.query.filter_by(category="todo", board_id=idnum)
	for each in query:
		elementdict = {
			'id': each.id,
			'board_id': each.board_id,
			'category': each.category,
			'created_at': each.created_at,
			'updated_at': each.updated_at,
			'description': each.description,
			'tags': []
			}
		returnList.append(elementdict)
	return returnList

def get_inprogress_list(idnum):
	returnList = []
	query = Board_Element.query.filter_by(category='inprogress', board_id=idnum)
	for each in query:
		elementdict = {
			'id': each.id,
			'board_id': each.board_id,
			'category': each.category,
			'created_at': each.created_at,
			'updated_at': each.updated_at,
			'description': each.description,
			'tags': []
			}
		returnList.append(elementdict)

	return returnList

def get_done_list(idnum):
	returnList = []
	query = Board_Element.query.filter_by(category='done', board_id=idnum)
	for each in query:
		elementdict = {
			'id': each.id,
			'board_id': each.board_id,
			'category': each.category,
			'created_at': each.created_at,
			'updated_at': each.updated_at,
			'description': each.description,
			'tags': []
			}
		returnList.append(elementdict)
	return returnList

def get_todo_count(idnum):
	return Board_Element.query.filter_by(category="todo", board_id=idnum).count()

def get_in_progress_count(idnum):
	return Board_Element.query.filter_by(category="inprogress",board_id=idnum).count()

def get_done_count(idnum):
	return Board_Element.query.filter_by(category="done", board_id=idnum).count()

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

def create_element(board_id, description, category):
	newElement = Board_Element(board_id=board_id, description=description, category=category)
	db.session.add(newElement)
	try:
		db.session.commit()
		return newElement
	except Exception as e:
		db.session.rollback()
		return e

def delete_element(element):
	db.session.delete(element)
	try:
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		return e

def advance_element(element):
	if element.category == 'todo':
		element.category = 'inprogress'
	elif element.category == 'inprogress':
		element.category = 'done'
	try:
		db.session.commit()
	except Exception as e:
		db.session.rollback()
		return e
	
