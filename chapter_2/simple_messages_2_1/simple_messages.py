stored_message = ""

def set_message(message):
    global stored_message

    if message == "":
        raise ValueError("Invalid message value")
    
    stored_message = message
    print(f"Message '{message}' stored") 