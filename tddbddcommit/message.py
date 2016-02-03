_valid_commit_kinds = ['INITIAL', 'RED', 'GREEN', 'REFACTOR', 'MERGE', 'BEIGE']


class MessageError(Exception):
    pass


class Message:
    max_summary_length = 75

    def __init__(self):
        self._kind = None
        self._summary = None
        self._body = None

    def kind(self, kind):
        if kind in _valid_commit_kinds:
            self._kind = kind
        else:
            raise MessageError('Invalid commit kind given')

    def summary(self, summary):
        if not summary:
            raise MessageError('No summary given')
        if not self._kind:
            raise MessageError('No commit kind given')
        self._summary = self._capitalise_first(summary)
        total_length = len(self._kind) + len(self._summary) + 1  # the space
        if total_length > self.max_summary_length:
            overflow = total_length - self.max_summary_length
            raise MessageError(
                'Given summary is ' + str(overflow) + ' character(s) too long')

    def body(self, body):
        self._body = body

    @staticmethod
    def _capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        if self._body:
            return self._kind + ' ' + self._summary + '\n\n' + self._body
        else:
            return self._kind + ' ' + self._summary
