from tddcommitmessage.messagebody import MessageBody
from tddcommitmessage import Kind

def test_message_is_wrapped_in_quotes():
    msg = MessageBody(Kind.red, 'Forty-two')
    assert str(msg) == '"RED Forty-two"'

def test_message_with_double_quote_is_wrapped_with_single():
    msg = MessageBody(Kind.red, 'But what are "Birds"?')
    assert str(msg) == r"""'RED But what are "Birds"?'"""

def test_first_letter_capitalised():
    msg = MessageBody(Kind.red, 'forty-two')
    assert str(msg) == '"RED Forty-two"'
