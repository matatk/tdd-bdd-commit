from tddcommitmessage.messagebody import MessageBody

def test_message_wrapped_in_quotes():
    msg = MessageBody('forty-two')
    assert str(msg) == '"forty-two"'
