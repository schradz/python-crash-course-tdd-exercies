from simple_messages import *

def test_simple_message_prints(capsys):
    test_message = "Hello World!"
    set_message(test_message)
    capture = capsys.readouterr()
    assert capture.out == "Hello World!\n"
    