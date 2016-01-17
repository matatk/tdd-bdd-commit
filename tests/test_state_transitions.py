import mock
import subprocess
import pytest
from tddbddcommit.state import State, StateTransitionError
from tddbddcommit import Kind


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


def test_merge_is_allowed_after_initial():
    state = State()
    state.change(Kind.initial)
    assert state.allowed(Kind.merge) is True


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

def _check_red_refactor_merge_and_beige_states_are_allowed(state):
    assert state.allowed(Kind.red) is True
    assert state.allowed(Kind.refactor) is True
    assert state.allowed(Kind.merge) is True
    assert state.allowed(Kind.beige) is True


#
# What is allowed after 'green'?
#

def test_states_allowed_after_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    _check_red_refactor_merge_and_beige_states_are_allowed(state)


#
# What is allowed after 'refactor'?
#

def test_states_allowed_after_refactor():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.refactor)
    _check_red_refactor_merge_and_beige_states_are_allowed(state)


#
# What is allowed after 'merge'?
#

def test_states_allowed_after_merge():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.merge)
    _check_red_refactor_merge_and_beige_states_are_allowed(state)


def test_refactor_not_allowed_after_merge_without_a_preceding_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.merge)
    assert state.allowed(Kind.refactor) is False


#
# What is allowed after 'beige'?
#

def test_states_allowed_after_beige():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.red)
    state.change(Kind.green)
    state.change(Kind.beige)
    _check_red_refactor_merge_and_beige_states_are_allowed(state)


def test_refactor_not_allowed_after_beige_without_a_preceding_green():
    state = State()
    state.change(Kind.initial)
    state.change(Kind.beige)
    assert state.allowed(Kind.refactor) is False


#
# Forcing a change to an invalid state raises
#

def test_changing_to_invalid_state_raises_error():
    with pytest.raises(StateTransitionError):
        state = State()
        state.change(Kind.green)


#
# Check through the git log to see if we've had a green before
#

def test_look_for_previous_green_commit_in_git_log():
    state = State()
    subprocess.Popen = mock.MagicMock()
    state.check_git_log()
    subprocess.Popen.assert_called_with(['git', 'log', '--pretty=format:"%s"'])


def test_test_green_found_in_log_check():
    fake_log = ('"GREEN"\n'
                '"RED Messages should be wrapped in quotes."\n'
                '"INITIAL"\n')
    state = State()
    subprocess.Popen = mock.MagicMock(return_value=fake_log)
    state.check_git_log()
    assert state._had_green is True


def test_test_no_green_found_in_log_check():
    fake_log = ('"RED Messages should be wrapped in quotes."\n'
                '"INITIAL"\n')
    state = State()
    subprocess.Popen = mock.MagicMock(return_value=fake_log)
    state.check_git_log()
    assert state._had_green is False
