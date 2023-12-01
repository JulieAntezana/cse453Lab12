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
    PUBLIC = 0,
    CONFIDENTIAL = 1,
    PRIVILEGED = 2,
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
    elif hasattr(obj, 'level'):
        # return the security level based on the level attribute
        if obj.level == "Secret":
            return Level.SECRET
        elif obj.level == "Privileged":
            return Level.PRIVILEGED
        elif obj.level == "Confidential":
            return Level.CONFIDENTIAL
        else:
            return Level.PUBLIC
    # otherwise, raise an exception
    else:
        raise TypeError("Invalid object type")
    
def security_condition_read(user, message):
    # get the security levels of the user and the message
    user_level = get_security_level(user)
    message_level = get_security_level(message)
    # apply the simple security rule: no read up
    return user_level >= message_level

def security_condition_write(user, message):
    # get the security levels of the user and the message
    user_level = get_security_level(user)
    message_level = get_security_level(message)
    # apply the star security rule: no write down
    return user_level <= message_level
 
