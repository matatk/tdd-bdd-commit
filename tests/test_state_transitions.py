from tddcommitmessage.state import State
from tddcommitmessage import Kind

def test_initial_allowed_first():
    state = State()
    assert state.allowed(Kind.initial) is True

def test_only_initial_allowed_first():
    state = State()
    assert state.allowed(None) is False

def test_red_allowed_after_initial():
    state = State()
    state.change(Kind.initial)
    assert state.allowed(Kind.red) is True

def test_green_allowed_after_red():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    assert state.allowed(Kind.green) is True

def test_refactor_is_allowed_after_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    assert state.allowed(Kind.refactor) is True

def test_red_is_allowed_after_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    assert state.allowed(Kind.red) is True

def test_merge_is_allowed_after_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    assert state.allowed(Kind.merge) is True

def test_red_is_allowed_after_refactor():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.refactor)
    assert state.allowed(Kind.red) is True

def test_merge_is_allowed_after_refactor():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.refactor)
    assert state.allowed(Kind.merge) is True
