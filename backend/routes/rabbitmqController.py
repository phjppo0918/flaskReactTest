from . import routes
from test_celery.celery import test_hello


@routes.route('/rabbit', methods=['get'])
def getRabbitMQ():
    a = 5
    while a > 0:
        test_hello.apply_async()

        a = a-1
    return 'ok'
