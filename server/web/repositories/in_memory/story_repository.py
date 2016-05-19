from deu_ruim.domain.repositories.story_repository import *
from copy import deepcopy
import cPickle as pickle
class InMemoryStoryRepository(StoryRepository):
    def __init__(self, stories=[]):
        self.stories = stories

    def persist_story(self, story):
        if(story.id != None):
            self.stories[story.id] = story
        else:
            story.id = len(self.stories)
            self.stories.append(story)
        return story

    def find_story(self, story_id):
        if story_id in range(len(self.stories)):
            return deepcopy(self.stories[story_id])
        return None

    def get_stories(self, time):
        return deepcopy(list(filter(lambda s: s.creation_time < time, self.stories))[-50:])

    def get_all_stories(self):
        return deepcopy(self.stories)

    def search_stories(self, tags, time):
        ranked_stories = sorted(map(lambda s: (len(tags.intersection(s.tags)), s.creation_time, s), self.stories))
        return deepcopy(list(map(lambda r: r[2], ranked_stories)))

class PersistentStoryRepository(InMemoryStoryRepository):
    def __init__(self, path):
        self.path = path
        try:
            stories = pickle.load(open(path, 'rb'))
        except:
            pickle.dump([],open(path,'wb'))
            stories = []
        InMemoryStoryRepository.__init__(self, stories)


    def persist_story(self, story):
        story = InMemoryStoryRepository.persist_story(self, story)
        pickle.dump(self.stories, open(self.path, 'wb'))
        return story
