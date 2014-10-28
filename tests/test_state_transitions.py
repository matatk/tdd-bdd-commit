from tddcommitmessage.state import State
from tddcommitmessage import Kinds

def test_initial_allowed_first():
    state = State()
    assert state.allowed(Kinds.initial)
