class InvalidAPIKeyError(Exception):
    def __init__(self, error):
        self.error = error


class NoAPIKeyError(Exception):
    def __init__(self, error):
        self.error = error


class APIError(Exception):
    def __init__(self, error):
        self.error = error


class NoInputError(Exception):
    def __init__(self, error):
        self.error = error
