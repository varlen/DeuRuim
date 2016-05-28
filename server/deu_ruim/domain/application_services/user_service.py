from deu_ruim.domain.entities.user import *

class UserService():
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, uid, name, surname, email, phone, msg_preference, car_tag):
        user = User(None, name, surname, email, phone, msg_preference, car_tag)
        return self.user_repository.persist_user(user)

    def remove_user(self, uid):
        return self.user_repository.remove_user(uid)

    def find_user(self, uid):
        return self.user_repository.find_user(uid)

    def edit_user(self, uid, name, surname, email, phone, msg_preference, car_tag):
        return self.user_repository.edit_user(uid, name, surname, email, phone, msg_preference, car_tag)

    def notify_user(self, car_tag, message):
        notified_users = []
        for user in self.user_repository.users:
            if user.car_tag == car_tag:
                # Needs implementation for send_message(user, message)
                # send_message(user, message)
                notified_users.append(user)
        return notified_users
