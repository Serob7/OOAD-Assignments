from abc import ABC, abstractmethod
from validators import not_empty_string

class Post(ABC):
    @abstractmethod
    def __init__(self, user, content, date_and_time):
        ...


class Text(Post):
    @not_empty_string('Content', 2)
    @not_empty_string('Date and time', 3)
    def __init__(self, user, content, date_and_time):
        self.user = user
        self.content = content
        self.date_and_time = date_and_time
        self.comments = []



class Image(Post):
    @not_empty_string('Content', 2)
    @not_empty_string('Date and time', 3)
    def __init__(self, user, content, date_and_time):
        self.user = user
        self.content = content
        self.date_and_time = date_and_time
        self.comments = []

