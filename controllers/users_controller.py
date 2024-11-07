from flask import jsonify


def get_all_users():
    try:
        print('##### Users_controller / get_all_users: TOIMII')
    except Exception as e:
        return jsonify({'err': str(e)}), 500

def get_user_by_id(id):
    print('##### Users_controller / get_user_by_id: TOIMII')

def create_user():
    print('##### Users_controller / create_user: TOIMII')

def update_user_by_id(id):
    print('##### Users_controller / update_user_by_id: TOIMII')

def delete_user_by_id(id):
    print('##### Users_controller / delete_user_by_id: TOIMII')