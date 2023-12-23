from rest_framework.response import Response


class ResponseHandler:

    def __init__(self, body):
        self.response = Response()
        self.body = {'msg': body}
        self.response.data = self.body

    def success_response(self):
        self.response.status_code = 200
        return self.response

    def error_response(self):
        self.response.status_code = 422
        return self.response
