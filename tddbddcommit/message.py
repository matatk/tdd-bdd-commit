_valid_commit_kinds = ['INITIAL', 'RED', 'GREEN', 'REFACTOR', 'MERGE', 'BEIGE']


class MessageSummaryError(Exception):
    pass


class Message:
    max_summary_length = 75

    def __init__(self, kind, message):
        if not message:
            raise MessageSummaryError('No message given')
        self._message = self._capitalise_first(message)
        if not kind:
            raise MessageSummaryError('No commit kind given')
        if kind not in _valid_commit_kinds:
            raise MessageSummaryError('Invalid commit kind given')
        self._kind = kind
        total_length = len(self._kind) + len(self._message) + 1  # the space
        if total_length > self.max_summary_length:
            overflow = total_length - self.max_summary_length
            raise MessageSummaryError(
                'Given message is ' + str(overflow) + ' character(s) too long')

    @staticmethod
    def _capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        if '"' in self._message:
            return "'" + self._kind + ' ' + self._message + "'"
        else:
            return '"' + self._kind + ' ' + self._message + '"'
