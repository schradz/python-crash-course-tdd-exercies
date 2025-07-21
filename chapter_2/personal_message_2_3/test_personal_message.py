import pytest
import personal_message

@pytest.fixture
def setup(request):
    personal_message.recipient = request.param[0]
    personal_message.message = request.param[1]

@pytest.mark.parametrize('setup', [('', 'Hello tester!')], indirect=True)
def test_print_message_throws_error_with_no_recipient(setup):
    with pytest.raises(ValueError) as e_info:
        personal_message.send_message()
    assert str(e_info.value) == "No recipient for message"

@pytest.mark.parametrize('setup', [('Tester', '')], indirect=True)
def test_print_message_throws_error_with_no_message(setup):
    with pytest.raises(ValueError) as e_info:
        personal_message.send_message()
    assert str(e_info.value) == "No message to send"

@pytest.mark.parametrize('setup', [('Tester', 'Hello tester!')], indirect=True)
def test_print_message_outputs_recipient_and_message(capsys, setup):
    personal_message.send_message()
    capture = capsys.readouterr()
    assert capture.out == "Sending message to Tester: Hello tester!\n"
