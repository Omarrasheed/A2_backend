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
	if request.args.get('id') == None:
		query = boards_dao.all_boards()
		jsonList = []
		for each in query:
			todo_count = boards_dao.get_all_todo()
			inprogress_count = boards_dao.get_all_in_progess()
			done_count = boards_dao.get_all_done()
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
