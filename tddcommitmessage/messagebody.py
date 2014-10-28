class MessageBody:
    def __init__(self, kind, message):
        self._message = message
        self._kind = kind

    def __str__(self):
        if '"' in self._message:
            return "'" + self._kind + ' ' + self._message + "'"
        else:
            return '"' + self._kind + ' ' + self._message + '"'
