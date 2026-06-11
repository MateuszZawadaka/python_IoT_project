import pyads

ALARM_DEFINITION = (
    ('bSafety', pyads.PLCTYPE_BOOL, 1),
    ('bPersistentsLost', pyads.PLCTYPE_BOOL, 1),
    ('bEthercatDevicesError', pyads.PLCTYPE_BOOL, 1),
    ('bWasherHighLevelTankSensor', pyads.PLCTYPE_BOOL, 1),
    ('bWasherLowLevelTankSensor', pyads.PLCTYPE_BOOL, 1),
    ('bWasherVeryLowLevelSensor', pyads.PLCTYPE_BOOL, 1),
    ('bCoccolinoHighLevelSensor', pyads.PLCTYPE_BOOL, 1),
    ('bCoccolinoLowLevelSensor', pyads.PLCTYPE_BOOL, 1),
    ('bCoccolinoVeryLowLevelSensor', pyads.PLCTYPE_BOOL, 1),
    ('bNaburexTemperatureBelowThreshold', pyads.PLCTYPE_BOOL, 1),
    ('bNaburexTemperatureOverThreshold', pyads.PLCTYPE_BOOL, 1),
    ('bCabinetEStopPressed', pyads.PLCTYPE_BOOL, 1),
    ('bHmiEStopPressed', pyads.PLCTYPE_BOOL, 1),
    ('bLeftChamberEStopPressed', pyads.PLCTYPE_BOOL, 1),
    ('bRightChamberEStopPressed', pyads.PLCTYPE_BOOL, 1),
    ('bDryingEStopPressed', pyads.PLCTYPE_BOOL, 1),
)

ALARM_MESSAGES = {
    "bSafety": "Safety alarm",
    "bPersistentsLost": "PLC persistents lost",
    "bEthercatDevicesError": "EtherCAT device error",
    "bCabinetEStopPressed": "Cabinet E-STOP pressed",
}