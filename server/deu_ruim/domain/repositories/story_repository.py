class StoryRepository():

    def get_stories(self, start_time):
        raise NotImplementedError

    def get_all_stories(self):
        raise NotImplementedError

    def search_stories(self, tags, start_time):
        raise NotImplementedError

    def find_story(self, id):
        raise NotImplementedError

    def persist_story(self, story):
        raise NotImplementedError


