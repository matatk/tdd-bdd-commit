import pytest
from tddcommitmessage.messagebody import MessageBody, MessageBodyError
from tddcommitmessage import Kind

def test_message_is_wrapped_in_quotes():
    msg = MessageBody(Kind.red, 'Forty-two')
    assert str(msg) == '"RED Forty-two"'

def test_first_letter_capitalised():
    msg = MessageBody(Kind.red, 'forty-two')
    assert str(msg) == '"RED Forty-two"'

def test_message_with_double_quote_is_wrapped_with_single():
    msg = MessageBody(Kind.red, 'But what are "Birds"?')
    assert str(msg) == r"""'RED But what are "Birds"?'"""

def test_long_message_raises_error():
    max_length = 75
    max_red_length = max_length - 1 - len(Kind.red)
    long_message = '@' * (max_red_length + 1)
    with pytest.raises(MessageBodyError) as excinfo:
        MessageBody(Kind.red, long_message)
    assert '1 character(s) too long' in str(excinfo.value)
