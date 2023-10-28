from validators import not_empty_string, email_checker
from abc import ABC, abstractmethod
from conversation import Conversation
from message import Text, Multimedia

class MessagingOperation(ABC):
    @abstractmethod
    def create_conversation(self):
        pass
    @abstractmethod
    def participate_in_convo(self, conversation):
        pass
    @abstractmethod
    def send_text_message(self, other, conversation, content):
        pass
    @abstractmethod
    def send_multimedia_message(self, other, conversation, content):
        ...
    @abstractmethod
    def receive_message(self):
        pass

    @abstractmethod
    def messaging_settings(self):
        pass

class User(MessagingOperation):
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.received_messages = []
        self.sent_messages = []

    def create_conversation(self):
        convo = Conversation(self)
        text = 'Created a new conversation'
        convo.conversation_history.append(text)
        print(text)

    def participate_in_convo(self, conversation):
        text = "I didn't create but I am participating in this conversation"
        conversation.conversation_history.append(text)
        print(text)

    def send_text_message(self, other, conversation, content):
        if isinstance(other, User):
            message = Text(self, conversation, content)
            self.sent_messages.append(message)
            conversation.conversation_history.append(message)
            other.received_messages.append(message)
            print('Sent')

    def send_multimedia_message(self, other, conversation, content):
        if isinstance(other, User):
            message = Multimedia(self, conversation, content)
            self.sent_messages.append(message)
            conversation.conversation_history.append(message)
            other.received_messages.append(message)
            print('Sent')

    def receive_message(self):
        for message in self.received_messages:
            message.conversation.conversation_history.append(message)
            print(f'Received from {message.user.name}')
            print(message.content)

    def messaging_settings(self):
        print('Settings changed')