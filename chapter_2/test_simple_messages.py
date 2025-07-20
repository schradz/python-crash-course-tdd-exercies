import pytest

import simple_messages
from simple_messages import set_message

@pytest.fixture(autouse=True)
def reset_store_message():
    simple_messages.stored_message = ""
    yield

def test_simple_message_prints_stored_value(capsys):
    test_message = "Hello World!"
    set_message(test_message)
    capture = capsys.readouterr()
    assert capture.out == "Message 'Hello World!' stored\n"

def test_simple_message_is_stored():
    test_message = "Hello World!"
    set_message(test_message)
    assert simple_messages.stored_message == "Hello World!"