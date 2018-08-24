class DirectionError(ValueError):

    def __init__(self, message):
        super(DirectionError, self).__init__(message)
