class CreateStoryService():
    def __init__(self, story_repository):
        self.story_repository = story_repository

    def create_story(self, title, description, lat, lon, tags=[]):
        story = Story(None, title, description, Location(lat,lon), set(tags))
        return self.story_repository.persist_story(story)
