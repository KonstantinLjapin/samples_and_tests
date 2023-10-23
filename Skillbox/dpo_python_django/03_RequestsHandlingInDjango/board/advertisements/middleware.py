from datetime import datetime
import logging


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_datetime = datetime.now()

        response = self.get_response(request)
        logging.basicConfig(filename="sample.log", level=logging.INFO)
        logging.info(f'{current_datetime}:{request.method}')

        return response
