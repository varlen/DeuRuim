import time
from deu_ruim.domain.entities.story import *
from deu_ruim.domain.value.location import *

class StoryService():
    def __init__(self, story_repository):
        self.story_repository = story_repository

    def create_story(self, title, description, lat, lon, tags=[]):
        story = Story(None, title, description, Location(lat, lon), tags)
        return self.story_repository.persist_story(story)

    def search_story(self, tags, time_max=None):
        return self.story_repository.search_stories(set(tags), time_max or time.time())
    
    def disqualify_story(self, story_id):
        story = self.story_repository.find_story(story_id)
        if story != None:
            story.disqualify()
            self.story_repository.persist_story(story)
            return story
        return None

    def get_stories(self, time):
        return self.story_repository.get_stories(time)

    def get_all_stories(self):
        return self.story_repository.get_all_stories()
