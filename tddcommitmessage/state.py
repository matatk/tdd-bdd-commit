from tddcommitmessage import Kinds

class State:
    def __init__(self):
        self._current_state = None

    def allowed(self, proposed_state):
        if not self._current_state:
            if proposed_state == Kinds.initial:
                return True
        elif self._current_state == Kinds.initial:
            if proposed_state == Kinds.red:
                return True
        elif self._current_state == Kinds.red:
            if proposed_state == Kinds.green:
                return True
        elif self._current_state == Kinds.green:
            if proposed_state == Kinds.refactor:
                return True
            elif proposed_state == Kinds.red:
                return True
            elif proposed_state == Kinds.merge:
                return True
        elif self._current_state == Kinds.refactor:
            if proposed_state == Kinds.red:
                return True
            elif proposed_state == Kinds.merge:
                return True
        return False

    def change(self, to_state):
        if self.allowed(to_state):
            self._current_state = to_state
