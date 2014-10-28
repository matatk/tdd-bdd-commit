from tddcommitmessage import Kinds

class State:
    def __init__(self):
        self._current_state = None

    def allowed(self, next_state):
        if not self._current_state:
            if next_state == Kinds.initial:
                return True
        elif self._current_state == Kinds.initial:
            if next_state == Kinds.red:
                return True
        return False

    def change(self, state):
        if self.allowed(state):
            self._current_state = state
