_valid_commit_kinds = ['INITIAL', 'RED', 'GREEN', 'REFACTOR', 'MERGE', 'BEIGE']


class MessageSummaryError(Exception):
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
            raise MessageSummaryError('Invalid commit kind given')

    def summary(self, summary):
        if not summary:
            raise MessageSummaryError('No message given')
        self._summary = self._capitalise_first(summary)
        total_length = len(self._kind) + len(self._summary) + 1  # the space
        if total_length > self.max_summary_length:
            overflow = total_length - self.max_summary_length
            raise MessageSummaryError(
                'Given message is ' + str(overflow) + ' character(s) too long')

    @staticmethod
    def _capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        if '"' in self._summary:
            return "'" + self._kind + ' ' + self._summary + "'"
        else:
            return '"' + self._kind + ' ' + self._summary + '"'
