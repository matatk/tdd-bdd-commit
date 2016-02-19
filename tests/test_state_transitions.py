from tddbddcommit import Kind
from tddbddcommit.state import allowed


# Before any state transitions, only 'initial' is allowed

def test_initial_is_allowed_first():
    assert allowed(None, Kind.initial) is True


def test_only_initial_is_allowed_first():
    assert allowed(None, Kind.red) is False


# What is allowed after 'initial'?

def test_red_is_allowed_after_initial():
    assert allowed(Kind.initial, Kind.red) is True


def test_merge_is_allowed_after_initial():
    assert allowed(Kind.initial, Kind.merge) is True


def test_beige_is_allowed_after_initial():
    assert allowed(Kind.initial, Kind.beige) is True


# What is allowed after 'red'?

def test_green_is_allowed_after_red():
    assert allowed(Kind.red, Kind.green) is True


# Common test for when Red, Refactor, Merge and Beige should be allowed

def _check_red_refactor_merge_beige_states_are_allowed(current):
    assert allowed(current, Kind.red) is True
    assert allowed(current, Kind.refactor) is True
    assert allowed(current, Kind.merge) is True
    assert allowed(current, Kind.beige) is True


# What is allowed after 'green'?

def test_states_allowed_after_green():
    _check_red_refactor_merge_beige_states_are_allowed(Kind.green)


# What is allowed after 'refactor'?

def test_states_allowed_after_refactor():
    _check_red_refactor_merge_beige_states_are_allowed(Kind.refactor)


# What is allowed after 'merge'?

def test_states_allowed_after_merge():
    _check_red_refactor_merge_beige_states_are_allowed(Kind.merge)


# What is allowed after 'beige'?

def test_states_allowed_after_beige():
    _check_red_refactor_merge_beige_states_are_allowed(Kind.beige)
