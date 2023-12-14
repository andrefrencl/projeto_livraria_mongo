from pymongo import MongoClient
from pymongo.server_api import ServerApi


class ClientFactory:

    def get_client(self):
        # no mongoatlas, connect, driver, escolher python e copiar URL
        return MongoClient(
            'mongodb+srv://fiap:o9wFIJBRxrNODc1N@cluster0.rw8b5oe.mongodb.net/?retryWrites=true&w=majority',
            server_api=ServerApi('1'))
