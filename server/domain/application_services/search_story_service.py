import time

class SearchStoryService():
    def __init__(self, story_repository):
        self.story_repository = story_repository

    def search_story(self, tags, time_max=None):
        return self.story_repository.search_stories(set(tags), time_max or time.time())
