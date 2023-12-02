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


def get_security_level(obj):
    # check if the object is a user
    if hasattr(obj, 'name'):
        # return the security level based on the username
        if obj.name == "AdmiralAbe":
            return Level.SECRET
        elif obj.name == "CaptainCharlie":
            return Level.PRIVILEGED
        elif obj.name.startswith("Seaman"):
            return Level.CONFIDENTIAL
        else:
            return Level.PUBLIC
    # check if the object is a message
    elif hasattr(obj, '_text_control'):
        print(f"_text_control: {obj._text_control}")
        text_control = obj._text_control.lower()
        print(f"text_control: {obj._text_control}")
        # return the security level based on the level attribute
        if obj._text_control == "Secret":
            return Level.SECRET
        elif obj._text_control == "Privileged":
            return Level.PRIVILEGED
        elif obj._text_control == "Confidential":
            return Level.CONFIDENTIAL
        elif obj._text_control == "Public":
            return Level.PUBLIC
        else:
            return Level.PUBLIC
    # otherwise, raise an exception
    else:
        print("Error: Invalid object type")
        return
        #raise TypeError("Invalid object type")
    
def is_authorized(user_level, text_control, mode):
    # check if the user is authorized to read or write the message, based on the Bell-LaPadula rules
    if mode == "read":
        # no read up
        return user_level.value >= text_control.value
    elif mode == "write":
        # no write down
        return user_level.value <= text_control.value
    else:
        # invalid mode
        return False

 
