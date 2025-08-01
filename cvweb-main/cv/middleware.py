import logging

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def __call__(self, request):
        path = request.path
        if not path.startswith('/static/') and not path.startswith('/admin/'):
            client_ip = self.get_client_ip(request)
            logging.info(f"IP: {client_ip}, Path: {request.path}, Method: {request.method}")
        return self.get_response(request)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')