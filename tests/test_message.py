import pytest
from tddbddcommit.message import Message, MessageSummaryError
from tddbddcommit import Kind


#
# Kind Validity
#

def test_invalid_kind_raises_error():
    with pytest.raises(MessageSummaryError) as excinfo:
        msg = Message()
        msg.kind(42)
    assert 'Invalid commit kind given' in str(excinfo.value)


#
# Message Validity
#

def test_empty_message_raises_error():
    with pytest.raises(MessageSummaryError) as excinfo:
        msg = Message()
        msg.kind(Kind.red)
        msg.summary(None)
    assert 'No message given' in str(excinfo.value)


def test_long_message_raises_error():
    max_length = 75
    max_red_length = max_length - 1 - len(Kind.red)
    long_message = '@' * (max_red_length + 1)
    with pytest.raises(MessageSummaryError) as excinfo:
        msg = Message()
        msg.kind(Kind.red)
        msg.summary(long_message)
    assert '1 character(s) too long' in str(excinfo.value)


#
# String handling
#

def test_message_is_wrapped_in_quotes():
    msg = Message()
    msg.kind(Kind.red)
    msg.summary('Forty-two')
    assert str(msg) == '"RED Forty-two"'


def test_first_letter_capitalised():
    msg = Message()
    msg.kind(Kind.red)
    msg.summary('forty-two')
    assert str(msg) == '"RED Forty-two"'


def test_message_with_double_quote_is_wrapped_with_single():
    msg = Message()
    msg.kind(Kind.red)
    msg.summary('But what are "Birds"?')
    assert str(msg) == r"""'RED But what are "Birds"?'"""
