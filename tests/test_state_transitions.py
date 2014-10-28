from tddcommitmessage.state import State
from tddcommitmessage import Kinds

def test_initial_allowed_first():
    state = State()
    assert state.allowed(Kinds.initial) is True

def test_only_initial_allowed_first():
    state = State()
    assert state.allowed(None) is False
