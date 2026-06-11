import time
import pyads
import config
import messageSender

from alarmsMonitor import AlarmMonitor


def main():
    sender = messageSender.MessageSender(
        config.API_URL,
        config.USERNAME,
        config.PASSWORD,
        config.PHONE_NUMBER
    )

    plc = pyads.Connection(
        config.AMS_NET_ID,
        config.AMS_PORT
    )

    plc.open()

    monitor = AlarmMonitor(
        plc=plc,
        sender=sender,
        config=config
    )

    while True:

        try:
            monitor.process()

        except Exception as e:
            print(f"Alarm processing error: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()