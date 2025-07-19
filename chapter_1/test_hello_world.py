from hello_world import *

def test_hello_world(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out == 'Hello World!\n'