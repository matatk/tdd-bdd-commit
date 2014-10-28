from tddcommitmessage import Kinds

class State:
    def allowed(self, next_state):
        if next_state == Kinds.initial:
            return True
        return False

    def change(self, state):
        pass
