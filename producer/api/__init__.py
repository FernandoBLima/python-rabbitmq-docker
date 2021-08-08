import logging

from aiohttp import web

from api.enum import EnvironmentVariables
from api.gateway.rabbitmq import RabbitMQ
from api.services.handler import Handler


async def health_status(request):
    return web.Response(text='UP')


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    rabbitMQ_instance = RabbitMQ(
        queue=EnvironmentVariables.RABBITMQ_QUEUE.get_env(),
        host=EnvironmentVariables.RABBITMQ_HOST.get_env(),
        routing_key=EnvironmentVariables.RABBITMQ_ROUTING_KEY.get_env(),
        username=EnvironmentVariables.RABBITMQ_USERNAME.get_env(),
        password=EnvironmentVariables.RABBITMQ_PASSSWORD.get_env(),
        exchange=EnvironmentVariables.RABBITMQ_EXCHANGE.get_env()
    )

    app = web.Application()
    handler = Handler(rabbitMQ_instance)

    app.add_routes([
        web.get('/', health_status),
        web.post('/', handler.publish),
    ])

    web.run_app(
        app,
        port=7000
    )
