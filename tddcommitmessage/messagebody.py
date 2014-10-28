class MessageBodyError(Exception):
    pass


class MessageBody:
    def __init__(self, kind, message):
        self._message = self._capitalise_first(message)
        self._kind = kind

    @staticmethod
    def _capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        if '"' in self._message:
            return "'" + self._kind + ' ' + self._message + "'"
        else:
            return '"' + self._kind + ' ' + self._message + '"'
