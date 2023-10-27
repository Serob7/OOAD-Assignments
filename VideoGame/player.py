from validators import not_empty_string, email_checker
class Player:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.progress = 0

    def play(self):
        print('Playing ..,')
        self.progress += 1

    def compete(self, other):
        if isinstance(other, Player):
            if self.progress > other.progress:
                print(f'{self.name} won!')
            else:
                print(f'{self.name} lost!')

