import messageSender

if __name__ == "__main__":
    sender = messageSender.MessageSender("https://api.sms-gate.app/3rdparty/v1/messages", "QTOOUX", "yzafpq_ulkxmxt")
    sender.send_message(device_id="vEfphj6hPyab3rpqtTMcK", message="Hello, this is a test message2!", phone_number="+48790648425")