recipient = ""
message = ""

def send_message():
    global recipient
    global message
    if recipient == "":
        raise ValueError("No recipient for message")
    if message == "":
        raise ValueError("No message to send")
    print(f"Sending message to {recipient}: {message}")