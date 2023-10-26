from validators import not_empty_string

class Comment:
    @not_empty_string('Content', 3)
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content