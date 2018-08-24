class BoundariesError(ValueError):

    def __init__(self, message):
        super(BoundariesError, self).__init__(message)
