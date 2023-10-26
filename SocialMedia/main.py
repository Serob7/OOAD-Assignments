from user import User
from post import Text, Image
from comment import Comment

def main():
    #creaete User instance
    user = User('Serob', 'serob@gmail.com')

    #create and view posts, leave comments, and manage their profile information
    text = user.create_text('Hello everyone!!!', '25.10.23 22:00')
    image = user.create_image('Nice Imange', '18.10.23 14:00')
    user.leave_comment(image, 'Very beautiful')
    user.leave_comment(text, 'Hello!')
    print(text.comments)
    print(image.comments)

if __name__ == '__main__':
    main()