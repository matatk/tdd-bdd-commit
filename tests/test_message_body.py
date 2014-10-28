from tddcommitmessage.messagebody import MessageBody

def test_message_is_wrapped_in_quotes():
    msg = MessageBody('forty-two')
    assert str(msg) == '"forty-two"'

def test_message_with_double_quote_is_wrapped_with_single():
    msg = MessageBody('But what are "Birds"?')
    assert str(msg) == r"""'But what are "Birds"?'"""
