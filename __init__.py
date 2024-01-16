from mycroft import MycroftSkill, intent_file_handler


class Esawksp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('esawksp.intent')
    def handle_esawksp(self, message):
        self.speak_dialog('esawksp')


def create_skill():
    return Esawksp()

