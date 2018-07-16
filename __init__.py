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
        
    def initialize(self):
        # load the jokes from the jokes directory
        #with open(self.path_to_joke_file) as f:
        #    self.jokes.append(f.readline().strip().split(':'))
        f = open(self.path_to_joke_file)
        for line in f.readlines():
            self.jokes.append(line.strip().split(':'))
        f.close()
        LOGGER.info('KnockKnockJokesSkill: Available jokes = ' + str(self.jokes))

    @intent_handler(IntentBuilder('handle_tell_joke').require('knock-knock').optionally('joke'))
    def handle_tell_joke(self, message):
        LOGGER.info('KnockKnockJokesSkill: handle_tell_joke')
        self.joke = choice(self.jokes)
        self.stage = 1
        self.speak_dialog('knock-knock', expect_response=True)  # expect 'who's there'

    def converse(self, utterances, lang="en-us"):
        if utterances != None:
            LOGGER.info('KnockKnockJokesSkill: utterance = ' + str(utterances))
            LOGGER.info('KnockKnockJokesSkill: joke = ' + str(self.joke))
            LOGGER.info('KnockKnockJokesSkill: stage = ' + str(self.stage))
            if self.stage == 1 and "who's there" in utterances:
                LOGGER.info('KnockKnockJokesSkill: Processing stage 1')
                self.speak(self.joke[0], expect_response=True)  # expect 'who'
                self.stage = 2
                return True
            if self.stage == 2 and 'who' in utterances[0].split(): 
                self.speak(self.joke[1])
                self.stage = 0
                self.joke = None
                return True
            else:
                return False
        else:
            LOGGER.info('KnockKnockJokesSkill: Received a NULL utterance. Why??')
            return False

    def stop(self):
        self.stage = 0
self.joke = None

def create_skill():
    return KnockKnockJokes()

