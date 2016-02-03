import pytest
from tddbddcommit.messagebody import MessageSummary, MessageSummaryError
from tddbddcommit import Kind


#
# String handling
#

def test_message_is_wrapped_in_quotes():
    msg = MessageSummary(Kind.red, 'Forty-two')
    assert str(msg) == '"RED Forty-two"'


def test_first_letter_capitalised():
    msg = MessageSummary(Kind.red, 'forty-two')
    assert str(msg) == '"RED Forty-two"'


def test_message_with_double_quote_is_wrapped_with_single():
    msg = MessageSummary(Kind.red, 'But what are "Birds"?')
    assert str(msg) == r"""'RED But what are "Birds"?'"""


#
# Message Validity
#

def test_long_message_raises_error():
    max_length = 75
    max_red_length = max_length - 1 - len(Kind.red)
    long_message = '@' * (max_red_length + 1)
    with pytest.raises(MessageSummaryError) as excinfo:
        MessageSummary(Kind.red, long_message)
    assert '1 character(s) too long' in str(excinfo.value)


def test_empty_message_raises_error():
    with pytest.raises(MessageSummaryError) as excinfo:
        MessageSummary(Kind.red, None)
    assert 'No message given' in str(excinfo.value)


#
# Kind Validity
#

def test_empty_kind_raises_error():
    with pytest.raises(MessageSummaryError) as excinfo:
        MessageSummary(None, '42')
    assert 'No commit kind given' in str(excinfo.value)


def test_invalid_kind_raises_error():
    with pytest.raises(MessageSummaryError) as excinfo:
        MessageSummary(42, '42')
    assert 'Invalid commit kind given' in str(excinfo.value)
