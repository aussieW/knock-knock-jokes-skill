from os.path import abspath, join, dirname
from random import choice

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util import wait_while_speaking

from mycroft.util.log import getLogger
LOGGER = getLogger(__name__)


class KnockKnockJokes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.jokes = []
        self.joke = None
        self.stage = 0
        self.path_to_joke_file = join(abspath(dirname(__file__)), 'jokes', 'jokes.txt')

    @intent_file_handler('jokes.knock.knock.intent')
    def handle_jokes_knock_knock(self, message):
        self.speak_dialog('jokes.knock.knock')


def create_skill():
    return KnockKnockJokes()

