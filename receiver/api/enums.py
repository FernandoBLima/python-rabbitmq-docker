import os
from enum import Enum


class EnvironmentVariables(str, Enum):
    RABBITMQ_USERNAME = 'RABBITMQ_USERNAME'
    RABBITMQ_PASSSWORD = 'RABBITMQ_PASSSWORD'
    RABBITMQ_HOST = 'RABBITMQ_HOST'
    RABBITMQ_QUEUE = 'RABBITMQ_QUEUE'
    RABBITMQ_ROUTING_KEY = 'RABBITMQ_ROUTING_KEY'
    RABBITMQ_EXCHANGE = 'RABBITMQ_EXCHANGE'
    SERVER_PORT = 'SERVER_PORT'
    SERVER_HOST = 'SERVER_HOST'

    def get_env(self, variable=None):
        return os.environ.get(self, variable)
