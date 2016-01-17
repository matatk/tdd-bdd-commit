import subprocess
from tddbddcommit import Kind


class StateTransitionError(Exception):
    pass


class State:
    def __init__(self):
        self._current_state = None
        self._had_green = False

    def allowed(self, proposed_state):
        if not self._current_state:
            if proposed_state is Kind.initial:
                return True
        elif self._current_state is Kind.initial:
            if (proposed_state is Kind.red or
               proposed_state is Kind.merge or
               proposed_state is Kind.beige):
                return True
        elif self._current_state is Kind.red:
            if proposed_state is Kind.green:
                return True
        elif (self._current_state is Kind.green or
              self._current_state is Kind.refactor or
              self._current_state is Kind.merge or
              self._current_state is Kind.beige):
            # Check to prevent refactors when there has been no green
            if (self._current_state is Kind.merge or
               self._current_state is Kind.beige):
                if proposed_state is Kind.refactor and not self._had_green:
                    return False
            # Otherwise allow all sensible state changes
            if (proposed_state is Kind.refactor or
               proposed_state is Kind.red or
               proposed_state is Kind.merge or
               proposed_state is Kind.beige):
                return True
        return False

    def change(self, to_state):
        if self.allowed(to_state):
            self._current_state = to_state
            if to_state is Kind.green:
                self._had_green = True
        else:
            raise StateTransitionError(
                'It is not valid to move from ' + str(self._current_state) +
                'to ' + str(to_state))

    def check_git_log(self):
        subprocess.Popen(['git', 'log', '--pretty=format:"%s"'])
