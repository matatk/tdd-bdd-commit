from tddcommit import Kind

class StateTransitionError(Exception):
    pass


class State:
    def __init__(self):
        self._current_state = None
        self._had_green = False

    def allowed(self, proposed_state):
        if not self._current_state:
            if proposed_state == Kind.initial:
                return True
        elif self._current_state == Kind.initial:
            if proposed_state == Kind.red \
            or proposed_state == Kind.merge \
            or proposed_state == Kind.beige:
                return True
        elif self._current_state == Kind.red:
            if proposed_state == Kind.green:
                return True
        elif self._current_state == Kind.green \
          or self._current_state == Kind.refactor \
          or self._current_state == Kind.merge \
          or self._current_state == Kind.beige:
            # Check to prevent refactors when there has been no green
            if self._current_state == Kind.beige \
            and proposed_state == Kind.refactor \
            and not self._had_green:
                return False
            # Otherwise allow all sensible state changes
            if proposed_state == Kind.refactor \
            or proposed_state == Kind.red \
            or proposed_state == Kind.merge \
            or proposed_state == Kind.beige:
                return True
        return False

    def change(self, to_state):
        if self.allowed(to_state):
            self._current_state = to_state
            if to_state is Kind.green:
                self._had_green = True
        else:
            raise StateTransitionError(
                'It is not valid to move from ' + str(self._current_state)
                + 'to ' + str(to_state))
