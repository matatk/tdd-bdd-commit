_valid_commit_kinds = ['INITIAL', 'RED', 'GREEN', 'REFACTOR', 'MERGE', 'BEIGE']
_max_summary_length = 75


class MessageError(Exception):
    pass


class Message:
    def __init__(self, kind, summary=None, body=None):
        self._kind = self._check_kind(kind)
        self._summary = self._check_summary(summary)
        self._body = body

    @staticmethod
    def _check_kind(kind):
        if kind in _valid_commit_kinds:
            return kind
        else:
            raise MessageError('Invalid commit kind given')

    def _check_summary(self, summary):
        if not summary:
            raise MessageError('No summary given')
        summary = Message.capitalise_first(summary)
        total_length = len(self._kind) + len(summary) + 1  # the space
        if total_length > _max_summary_length:
            overflow = total_length - _max_summary_length
            raise MessageError(
                'Given summary is ' + str(overflow) + ' character(s) too long')
        return summary

    @staticmethod
    def capitalise_first(string):
        return string[0].upper() + string[1:]

    def __str__(self):
        flattened = self._kind + ' ' + self._summary
        if self._body:
            flattened += '\n\n' + self._body
        return flattened
