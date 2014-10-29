import pytest
from tddcommit.state import State, StateTransitionError
from tddcommit import Kind
# FIXME if doing a beige after initial, it should not be possible to refactor after the beige

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
# Common test for when Red, Refactor, Merge and Beige should be allowed
#

def _check_standard_next_states_are_allowed(state):
    assert state.allowed(Kind.red) is True
    assert state.allowed(Kind.refactor) is True
    assert state.allowed(Kind.merge) is True
    assert state.allowed(Kind.beige) is True


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

def test_states_allowed_after_green(state_green):
    _check_standard_next_states_are_allowed(state_green)


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

def test_states_allowed_after_refactor(state_refactor):
    _check_standard_next_states_are_allowed(state_refactor)


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

def test_states_allowed_after_merge(state_merge):
    _check_standard_next_states_are_allowed(state_merge)


#
# What is allowed after 'beige'?
#

@pytest.fixture
def state_beige():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.beige)
    return state

def test_states_allowed_after_beige(state_beige):
    _check_standard_next_states_are_allowed(state_beige)


#
# Forcing a change to an invalid state raises
#

def test_changing_to_invalid_state_raises_error():
    with pytest.raises(StateTransitionError):
        state = State()
        state.change(Kind.green)
