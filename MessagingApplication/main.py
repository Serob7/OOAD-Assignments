from user import User
from conversation import Conversation

def main():
    #create User instance
    user = User('Serob', 'serob@gmail.com')
    user1 = User('Tom', 'tom@gmail.com')

    #create and participate in conversation
    user.create_conversation()
    conversation = Conversation(user1)
    user.participate_in_convo(conversation)

    #send and receive messages
    user.send_multimedia_message(user1, conversation, 'Hey Tom, how are you?')
    user1.receive_message()

    #settigns
    user.messaging_settings()


if __name__ == '__main__':
    main()