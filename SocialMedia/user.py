from abc import ABC, abstractmethod
from validators import not_empty_string, email_checker
from post import Image, Text
class Operations(ABC):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.mame = name
        self.contact_information = contact_information
        self.posts = {}


    @abstractmethod
    def create_image(self, content, date_and_time):
        ...

    @abstractmethod
    def create_text(self, content, date_and_time):
        ...
    @abstractmethod
    def view_post(self, name):
        ...
    @abstractmethod
    def leave_comment(self, post):
        ...
    @abstractmethod
    def manage_profile(self, name, contact_information):
        ...


class User(Operations):

    def create_image(self, content, date_and_time):
        image = Image(self, content, date_and_time)
        print(f"Image {image.content} has been posted at {image.date_and_time}")
        self.posts[image.content] = image
        return image


    def create_text(self, content, date_and_time):
        text = Text(self, content, date_and_time)
        print(f"Text {text.content} has been posted at {text.date_and_time}")
        self.posts[text.content] = text
        return text

    @not_empty_string('Content', 1)
    def view_post(self, content):
        if content in self.posts:
            print(self.posts[content].content, self.posts[content.date_and_time])
        else:
            print('Post not found')
    @not_empty_string('Text', 2)
    def leave_comment(self, post, text):
        post.comments.append(text)

    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def manage_profile(self):
        print('\tProfile information')
        print(f"Name - {self.name}, \nEmail - {self.contact_information}")
        for post in self.posts:
            print(f"{post.content}, {post.date_and_time}")
            for comment in post.comments:
                print(comment)



