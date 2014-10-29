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

@pytest.fixture
def state_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    return state

def test_refactor_is_allowed_after_green(state_green):
    assert state_green.allowed(Kind.refactor) is True

def test_red_is_allowed_after_green(state_green):
    assert state_green.allowed(Kind.red) is True

def test_merge_is_allowed_after_green(state_green):
    assert state_green.allowed(Kind.merge) is True

def test_beige_is_allowed_after_green(state_green):
    assert state_green.allowed(Kind.beige) is True


#
# What is allowed after 'refactor'?
#

@pytest.fixture
def state_refactor():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.refactor)
    return state

def test_refactor_is_allowed_after_refactor(state_refactor):
    assert state_refactor.allowed(Kind.refactor) is True

def test_red_is_allowed_after_refactor(state_refactor):
    assert state_refactor.allowed(Kind.red) is True

def test_merge_is_allowed_after_refactor(state_refactor):
    assert state_refactor.allowed(Kind.merge) is True


#
# What is allowed after 'merge'?
#

@pytest.fixture
def state_merge():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.merge)
    return state

def test_refactor_is_allowed_after_merge(state_merge):
    assert state_merge.allowed(Kind.refactor) is True

def test_red_is_allowed_after_merge(state_merge):
    assert state_merge.allowed(Kind.red) is True

def test_merge_is_allowed_after_merge(state_merge):
    assert state_merge.allowed(Kind.merge) is True


#
# Forcing a change to an invalid state raises
#

def test_changing_to_invalid_state_raises_error():
    with pytest.raises(StateTransitionError):
        state = State()
        state.change(Kind.green)
