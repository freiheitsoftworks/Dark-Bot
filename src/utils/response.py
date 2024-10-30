class Response:
    def __init__(self, message: str, status: int):
        self.message = message
        self.status = status

    @classmethod
    def right(cls, message: str):
        return cls(message, 200)

    @classmethod
    def left(cls, message: str, status: int):
        return cls(message, status)