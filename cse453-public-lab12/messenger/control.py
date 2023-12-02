########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Eric, Nichole, Nicholas, Julie, and Austin
# Summary:
#    This class stores the notion of Bell-LaPadula
########################################################################
# constants for security levels
from enum import Enum


class Level(Enum):
    PUBLIC = 0
    CONFIDENTIAL = 1
    PRIVILEGED = 2
    SECRET = 3


def parse_security_level(lvl: str):
    return Level.__getitem__(lvl.upper())


def access_rights(user_level, message_lvl, mode):
    # check if the user is authorized to read or write the message, based on the Bell-LaPadula rules
    if mode == "read":
        # no read up
        return user_level.value >= message_lvl.value
    if mode == "write":
        # no write down
        return user_level.value <= message_lvl.value
    # invalid mode
    return False
