from alarms import ALARM_DEFINITION, ALARM_MESSAGES

class AlarmMonitor:

    def __init__(self, plc, sender, config):
        self.plc = plc
        self.sender = sender
        self.config = config
        self.reported_alarms = set()

    def read_alarms(self):
        return self.plc.read_structure_by_name(
            self.config.STRUCTURE_NAME,
            ALARM_DEFINITION
        )

    def process(self):

        alarms = self.read_alarms()

        for alarm_name, active in alarms.items():

            if active and alarm_name not in self.reported_alarms:

                self._send_alarm(alarm_name)
                self.reported_alarms.add(alarm_name)

            elif active == False:
                self.reported_alarms.discard(alarm_name)

    def _send_alarm(self, alarm_name):

        message = ALARM_MESSAGES.get(
            alarm_name,
            alarm_name
        )

        self.sender.send_message(
            device_id=self.config.DEVICE_ID,
            phone_number=self.config.PHONE_NUMBER,
            message=f"MASHINE: {self.config.MACHINE_NAME} - ALARM: {message}"
        )

        print(f"ALARM: {message}")