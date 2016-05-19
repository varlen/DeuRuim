from deu_ruim.domain.repositories.story_repository import *
class InMemoryStoryRepository(StoryRepository):
    def __init__(self):
        self.stories = []

    def persist_story(self, story):
        story.id = len(self.stories)
        self.stories.append(story)
        return story

    def get_stories(self, time):
        return list(filter(lambda s: s.creation_time < time, self.stories))[-50:]

    def search_stories(self, tags, time):
        ranked_stories = sorted(map(lambda s: (len(tags.intersection(s.tags)), s), s.time, self.stories))

        return list(map(lambda r: r[2], ranked_stories))
