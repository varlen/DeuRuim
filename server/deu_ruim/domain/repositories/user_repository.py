class UserRepository():
    def persist_user(self, user):
        raise NotImplementedError
        
    def find_user(self, uid):
        raise NotImplementedError

    def remove_user(self, uid):
        raise NotImplementedError

    def edit_user(self, uid, name, surname, email, phone, msg_preference, car_tag):
        raise NotImplementedError
