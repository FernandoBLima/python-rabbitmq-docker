import logging

from api.enums import EnvironmentVariables
from api.gateway.rabbitmq import rabbitMQServer


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    server = rabbitMQServer(
        queue=EnvironmentVariables.RABBITMQ_QUEUE.get_env(),
        host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
        routing_key=EnvironmentVariables.RABBITMQ_ROUTING_KEY.get_env(),
        username=EnvironmentVariables.RABBITMQ_USERNAME.get_env(),
        password=EnvironmentVariables.RABBITMQ_PASSSWORD.get_env(),
        exchange=EnvironmentVariables.RABBITMQ_EXCHANGE.get_env(),
    )
    server.get_messages()
