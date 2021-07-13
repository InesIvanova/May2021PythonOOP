import os
from dotenv import load_dotenv

load_dotenv()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class ServicePaypal:
    def __init__(self,):
        self.secret_key = os.getenv('PAYPAL_API_KEY')