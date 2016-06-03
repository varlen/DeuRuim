class User():
    def __init__(self, uid, name, surname, email, phone=None, msg_preference='email', car_tag=None):
        self.uid = uid
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.msg_preference = msg_preference
        self.car_tag = car_tag

