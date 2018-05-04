from app.constants import *
from . import *
from flask import request

@kanban.route('/boards', methods=['POST'])
def post():
	title = request.args.get('title')
	board = boards_dao.create_board(title)
	query = boards_dao.board_by_title(title)
	return jsonify({'success': 'true',
					'data': {
						'board': {
							'board_elements': False,
							'created_at': query.created_at,
							'id': query.id,
							'title': query.title,
							'updated_at': query.updated_at
							}
						}
					})

@kanban.route('/boards', methods=['DELETE'])
def delete():
	idnum = request.args.get('id')
	query = boards_dao.board_by_id(idnum)
	boards_dao.delete_board(query)
	return jsonify({'success': True})

@kanban.route('/boards', methods=['GET'])
def get():
	query = boards_dao.all_boards()
	jsonList = []
	for each in query:
		todo_count = boards_dao.get_todo_count(each.id)
		inprogress_count = boards_dao.get_in_progress_count(each.id)
		done_count = boards_dao.get_done_count(each.id)
		jsonList.append({
			'created_at': each.created_at,
			'id': each.id,
			'updated_at': each.updated_at,
			'title': each.title,
			'todo_count': todo_count,
			'inprogress_count': inprogress_count,
			'done_count': done_count
			})
	return jsonify({'success': True,
					'data':{
						'boards': jsonList
						}})

		

@kanban.route('/board_elements', methods=['POST'])
def new_element():
	board_id = request.args.get('board_id')
	category = request.args.get('category')
	description = request.args.get('description')
	newelement = boards_dao.create_element(board_id, description, category)
	return jsonify ({'success': True,
					'data': {
						'board_element': {
							'id': newelement.id,
							'board_id': newelement.board_id,
							'category': newelement.category,
							'created_at': newelement.created_at,
							'updated_at': newelement.updated_at,
							'description': newelement.description,
							'tags': []
							}
						}
					})

@kanban.route('/board_elements', methods=['DELETE'])
def delete_element():
	element_id = request.args.get('board_element_id')
	query = boards_dao.element_by_id(element_id)
	boards_dao.delete_element(query)
	return jsonify ({'success': True})

@kanban.route('/boards/<idnum>', methods=['GET'])
def get_one_board(idnum):
	query = boards_dao.board_by_id(idnum)
	todos = boards_dao.get_todo_list(idnum)
	inprogress = boards_dao.get_inprogress_list(idnum)
	dones = boards_dao.get_done_list(idnum)
	return jsonify({'success': True,
					'data': {
						'board': {
							'id': query.id,
							'title': query.title,
							'created_at': query.created_at,
							'updated_at': query.updated_at,
							'todo': todos,
							'inprogress': inprogress,
							'done': dones
							}
						}
					})

@kanban.route('/board_elements/advance', methods=['POST'])
def advance():
	idnum = request.args.get('id')
	query = boards_dao.element_by_id(idnum)
	boards_dao.advance_element(query)
	return jsonify({'success': True})


