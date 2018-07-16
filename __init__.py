from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class KnockKnockJokes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('jokes.knock.knock.intent')
    def handle_jokes_knock_knock(self, message):
        self.speak_dialog('jokes.knock.knock')


def create_skill():
    return KnockKnockJokes()

