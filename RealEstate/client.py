from validators import not_empty_string, email_checker

class Client:
    @not_empty_string('Name', 1)
    @email_checker('Contact information', 2)
    def __init__(self, name, contact_information):
        self.name = name
        self.contact_information = contact_information
        self.properties = []

    def pruchase_property(self, property):
        print(f"I have purchased property at {property.address} for {property.price}")
        property.owner = self.name
        self.properties.append(property)
