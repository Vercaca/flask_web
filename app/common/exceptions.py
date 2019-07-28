class UnauthorizedException(Exception):
    status_code = 401

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class UnhandledException(Exception):
    status_code = 404

    def __init__(self, payload=None):
        Exception.__init__(self)
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = 'UnhandledException'
        return rv