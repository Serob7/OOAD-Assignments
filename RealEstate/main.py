from property import Residental, Commercial
from agent import Agent
from client import Client

def main():
    #create Property, Agent and CLient instances
    property = Residental('Yerevan', 75000, 'Smart home')
    property2 = Commercial('Abovyan', 120000, 'Furniture included')
    agent = Agent('Tom', 'tom@gmail.com')
    client = Client('Serob', 'serob@gmail.com')


    #purchase property
    client.pruchase_property(property)
    client.pruchase_property(property2)

    #property listing and client information
    agent.manage_listing(client)
    agent.client_info(client)

if __name__ == '__main__':
    main()