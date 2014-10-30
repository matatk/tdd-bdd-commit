class MessageBodyError(Exception):
    pass


class MessageBody:
    max_length = 75

    def __init__(self, kind, message):
        if not message:
            raise MessageBodyError('No message given')
        self._message = self._capitalise_first(message)
        if not kind:
            raise MessageBodyError('No commit kind given')
        self._kind = kind
        total_length = len(self._kind) + len(self._message) + 1  # the space
        if total_length > self.max_length:
            overflow = total_length - self.max_length
            raise MessageBodyError(
                'Given message is ' + str(overflow) + ' character(s) too long')

    @staticmethod
    def _capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        if '"' in self._message:
            return "'" + self._kind + ' ' + self._message + "'"
        else:
            return '"' + self._kind + ' ' + self._message + '"'
