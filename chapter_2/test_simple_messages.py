from simple_messages import *

def test_simple_message_prints_stored_value(capsys):
    test_message = "Hello World!"
    set_message(test_message)
    capture = capsys.readouterr()
    assert capture.out == "Message 'Hello World!' stored\n"

def test_simple_message_is_stored():
    test_message = "Hello World!"
    assert stored_message == ""
    set_message(test_message)
    assert stored_message == test_message
    