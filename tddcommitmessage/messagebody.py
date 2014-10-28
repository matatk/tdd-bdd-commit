class MessageBody:
    def __init__(self, message):
        self._message = message

    def __str__(self):
        if '"' in self._message:
            return "'" + self._message + "'"
        else:
            return '"' + self._message + '"'
