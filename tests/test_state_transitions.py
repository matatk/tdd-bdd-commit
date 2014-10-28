from tddcommitmessage.state import State
from tddcommitmessage import Kinds

def test_initial_allowed_first():
    state = State()
    assert state.allowed(Kinds.initial) is True

def test_only_initial_allowed_first():
    state = State()
    assert state.allowed(None) is False

def test_red_allowed_after_initial():
    state = State()
    state.change(Kinds.initial)
    assert state.allowed(Kinds.red) is True

def test_green_allowed_after_red():
    state = State()
    state.change(Kinds.initial)
    state.change(Kinds.red)
    assert state.allowed(Kinds.green) is True

def test_refactor_is_allowed_after_green():
    state = State()
    state.change(Kinds.initial)
    state.change(Kinds.red)
    state.change(Kinds.green)
    assert state.allowed(Kinds.refactor) is True

def test_red_is_allowed_after_green():
    state = State()
    state.change(Kinds.initial)
    state.change(Kinds.red)
    state.change(Kinds.green)
    assert state.allowed(Kinds.red) is True
