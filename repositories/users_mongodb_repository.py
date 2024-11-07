class UsersMongodbRepository:
    def __init__(self, con):
        self.con = con
    
    def get_all(self):
        print('##### users_mongodb_repository / get_all: TOIMII')
        print('##### users_mongodb_repository / get_all: CON ON:' + str(self.con))

    def get_by_id(self):
        print('##### users_mongodb_repository / get_by_id: TOIMII')
        print('##### users_mongodb_repository / get_by_id: CON ON:' + str(self.con))

    def create(self):
        print('##### users_mongodb_repository / create: TOIMII')
        print('##### users_mongodb_repository / create: CON ON:' + str(self.con))

    def update_by_id(self):
        print('##### users_mongodb_repository / update_by_id: TOIMII')
        print('##### users_mongodb_repository / update_by_id: CON ON:' + str(self.con))

    def delete_by_id(self):
        print('##### users_mongodb_repository / delete: TOIMII')
        print('##### users_mongodb_repository / delete: CON ON:' + str(self.con))