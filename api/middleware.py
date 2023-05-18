import logging
from datetime import datetime
import pytz

class ErrorLoggingMiddleware:
    status_codes=[404, 500, 502, 400, 401, 403, 502, 503, 504]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code in self.status_codes:
            logger = logging.getLogger('django')
            timezone = pytz.timezone('Asia/Kolkata')
            now = datetime.now(timezone)
            formatted_datetime = now.strftime("%d-%m-%Y %I:%M %p")
            logger.error(f"{response.status_code} {request.method} {request.path} {request.user} {formatted_datetime}")
        return response