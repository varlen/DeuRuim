import json

from flask import Flask, request, jsonify

from repositories.in_memory import *
from deu_ruim.domain.application_services import *

def render_story(story):
    story_d = story.__dict__.copy()
    story_d['location'] = story_d['location'].__dict__.copy()

    return story_d

def render_stories(stories):
    return {'stories': list(map(render_story, stories))}

app = Flask(__name__)

story_repository = InMemoryStoryRepository()
create_story_service = CreateStoryService(story_repository)
search_story_service = SearchStoryService(story_repository)

@app.route('/stories', methods=['GET'])
def get_stories():
    stories = search_story_service.search_story(["tag"])
    return jsonify(render_stories(stories))

@app.route('/stories', methods=['POST'])
def create_story():
    story = crate_story_service.create_story(
            "Deu Ruim",
            "Deu Ruim Mesmo", 
            0,
            0,
            ["tag"]
            )

    return json.dumps(render_story(story))

server_url = '127.0.0.1'
server_port = '5000'

def run():
    app.run(server_url)
