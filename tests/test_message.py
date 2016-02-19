import pytest
from tddbddcommit.message import Message, MessageError
from tddbddcommit import Kind


# Kind Validity

def test_invalid_kind_raises_error():
    with pytest.raises(MessageError) as excinfo:
        Message(42)
    assert 'Invalid commit kind given' in str(excinfo.value)


# Summary Validity

def test_empty_summary_raises_error():
    with pytest.raises(MessageError) as excinfo:
        Message(Kind.red)
    assert 'No summary given' in str(excinfo.value)


def test_long_summary_raises_error():
    max_length = 75
    max_red_length = max_length - 1 - len(Kind.red)
    long_message = '@' * (max_red_length + 1)
    with pytest.raises(MessageError) as excinfo:
        Message(Kind.red, long_message)
    assert '1 character(s) too long' in str(excinfo.value)


# Summary string handling

def test_first_letter_capitalised():
    msg = Message(Kind.red, 'forty-two')
    assert str(msg) == 'RED Forty-two'


# Full-format messages

def test_messgae_with_body_contains_blank_line():
    msg = Message(Kind.red, 'Forty-two', 'Amazing!')
    assert str(msg) == """RED Forty-two

Amazing!"""
