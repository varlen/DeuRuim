from deu_ruim.domain.repositories.user_repository import *
from copy import deepcopy
import cPickle as pickle

class InMemoryUserRepository(UserRepository):
    def __init__(self, users=[]):
        self.users = users

    def persist_user(self, user):
        if(user.uid is not None):
            self.users[user.uid] = user
        else:
            user.uid = len(self.users)
            self.users.append(user)
        return user

        
    def find_user(self, uid):
        if uid in range(len(self.users)):
            return deepcopy(self.users[uid])
        return None

    def remove_user(self, uid):
        return self.users.pop(uid)

    def edit_user(self, uid, name, surname, email, phone, msg_preference, car_tag):
        user = find_user(uid)
        if user is None:
            return None

        #modifying everything but uid
        user.name = name
        user.surname = surname
        user.email = email
        user.car_tag = car_tag
        user.phone = phone
        user.msg_preference = msg_preference

        return self.persist_user(user)

class PersistentUserRepository(InMemoryUserRepository):
    def __init__(self, path):
        self.path = path
        try:
            users = pickle.load(open(path+'users.pickle', 'rb'))
        except:
            pickle.dump([], open(path+'users.pickle','wb'))
            users = []
        InMemoryUserRepository.__init__(self, users)

    def persist_user(self, user):
        user = InMemoryUserRepository.persist_user(self, user)
        pickle.dump(self.users, open(self.path+'users.pickle','wb'))
        return user
