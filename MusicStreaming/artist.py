from validators import not_empty_string, email_checker

class Artist:
    @not_empty_string('Name', 1)
    @email_checker('Contact', 2)
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
