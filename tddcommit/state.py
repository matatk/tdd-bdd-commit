from tddcommit import Kind

class State:
    def __init__(self):
        self._current_state = None

    def allowed(self, proposed_state):
        if not self._current_state:
            if proposed_state == Kind.initial:
                return True
        elif self._current_state == Kind.initial:
            if proposed_state == Kind.red:
                return True
        elif self._current_state == Kind.red:
            if proposed_state == Kind.green:
                return True
        elif self._current_state == Kind.green:
            if proposed_state == Kind.refactor:
                return True
            elif proposed_state == Kind.red:
                return True
            elif proposed_state == Kind.merge:
                return True
        elif self._current_state == Kind.refactor:
            if proposed_state == Kind.refactor:
                return True
            elif proposed_state == Kind.red:
                return True
            elif proposed_state == Kind.merge:
                return True
        elif self._current_state == Kind.merge:
            if proposed_state == Kind.refactor:
                return True
            elif proposed_state == Kind.red:
                return True
            elif proposed_state == Kind.merge:
                return True
        return False

    def change(self, to_state):
        if self.allowed(to_state):
            self._current_state = to_state
