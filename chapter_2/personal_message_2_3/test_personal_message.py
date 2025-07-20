import pytest
import personal_message

def test_print_message_throws_error_with_no_recipient():
    personal_message.recipient = ""
    personal_message.message = "Hello tester!"
    with pytest.raises(ValueError) as e_info:
        personal_message.send_message()
    assert str(e_info.value) == "No recipient for message"

def test_print_message_throws_error_with_no_message():
    personal_message.message = ""
    personal_message.recipient = "Tester"
    with pytest.raises(ValueError) as e_info:
        personal_message.send_message()
    assert str(e_info.value) == "No message to send"

def test_print_message_outputs_recipient_and_message(capsys):
    personal_message.recipient = "Tester"
    personal_message.message = "Hello tester!"
    personal_message.send_message()
    capture = capsys.readouterr()
    assert capture.out == "Sending message to Tester: Hello tester!\n"

