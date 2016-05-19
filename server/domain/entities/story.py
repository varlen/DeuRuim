class Story():
    def __init__(self, rid, title, description, location, tags=set()):
        self.id = rid
        self.description = description
        self.location = location
        self.tags = tags
        self.creation_time = time.now
        self.disqualifications = 0

    def disqualify(self):
        self.disqualifications += 1
