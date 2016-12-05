from flask import jsonify

class APIError(Exception):
    error_name = 'unknown_error'
    status_code = 200

    def __init__(self, message, error_name=None, status_code=None,
                 details=None):
        Exception.__init__(self)

        if status_code is not None:
            self.status_code = status_code
        if error_name is not None:
            self.error_name = error_name

        self.details = None

    def to_response(self):
        rv = dict(message=self.message, error=self.error_name)
        if self.details:
            rv['details'] = details

        resp = jsonify(rv)
        resp.status_code = self.status_code
        return resp
