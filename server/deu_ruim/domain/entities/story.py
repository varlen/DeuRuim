import time
class Story():
    def __init__(self, rid, title, description, location, category, tags=set([])):
        self.id = rid
        self.title = title
        self.category  = category
        self.description = description
        self.location = location
        self.tags = tags
        self.creation_time = time.time()
        self.disqualifications = 0

    def disqualify(self):
        self.disqualifications += 1
