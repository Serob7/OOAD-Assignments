from abc import ABC, abstractmethod
from validators import not_empty_string

class Message(ABC):
    @abstractmethod
    def __init__(self, user, conversation, content):
        ...
class Text(Message):
    @not_empty_string('Content', 3)
    def __init__(self, user, conversation, content):
        self.user = user
        self.conversation = conversation
        self.content = content



class Multimedia(Message):
    @not_empty_string('Content', 3)
    def __init__(self, user, conversation, content):
        self.user = user
        self.conversation = conversation
        self.content = content


