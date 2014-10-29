import pytest
from tddcommit.state import State, StateTransitionError
from tddcommit import Kind

#
# Before any state transitions, only 'initial' is allowed
#

def test_initial_is_allowed_first():
    state = State()
    assert state.allowed(Kind.initial) is True

def test_only_initial_is_allowed_first():
    state = State()
    assert state.allowed(None) is False


#
# What is allowed after 'initial'?
#

def test_red_is_allowed_after_initial():
    state = State()
    state.change(Kind.initial)
    assert state.allowed(Kind.red) is True

def test_beige_is_allowed_after_initial():
    state = State()
    state.change(Kind.initial)
    assert state.allowed(Kind.beige) is True


#
# What is allowed after 'red'?
#

def test_green_is_allowed_after_red():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    assert state.allowed(Kind.green) is True


#
# What is allowed after 'green'?
#

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

def test_beige_is_allowed_after_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    assert state.allowed(Kind.beige) is True


#
# What is allowed after 'refactor'?
#

def test_refactor_is_allowed_after_refactor():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.refactor)
    assert state.allowed(Kind.refactor) is True

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


#
# What is allowed after 'merge'?
#

def test_refactor_is_allowed_after_merge():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.merge)
    assert state.allowed(Kind.refactor) is True

def test_red_is_allowed_after_merge():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.merge)
    assert state.allowed(Kind.red) is True

def test_merge_is_allowed_after_merge():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.merge)
    assert state.allowed(Kind.merge) is True


#
# Forcing a change to an invalid state raises
#

def test_changing_to_invalid_state_raises_error():
    with pytest.raises(StateTransitionError):
        state = State()
        state.change(Kind.green)
