########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class allows one user to interact with the system
########################################################################

import messages
import control

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password, level):
        self.name = name
        self.password = password
        self.level = level # added code: security level

userlist = [
   [ "AdmiralAbe",     "password", control.Level.SECRET ],  # added code: security level
   [ "CaptainCharlie", "password", control.Level.PRIVILEGED ], # added code: security level
   [ "SeamanSam",      "password", control.Level.CONFIDENTIAL ], # added code: security level
   [ "SeamanSue",      "password", control.Level.CONFIDENTIAL ], # added code: security level
   [ "SeamanSly",      "password", control.Level.CONFIDENTIAL ],
   [ "Murffkins",      "password", control.Level.PUBLIC ] # added code: security level
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username, password, messages):
        self._user_level = self.authenticate(username, password)
        self._username = username
        self._p_messages = messages
        #self._level = level # added code: security level
    def get_user_level(self):  # New getter method
        return self._user_level

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################

    def show(self):
        id_ = self._prompt_for_id("display") #Get the message id from the user input
        print(f"ID: {id_}")
        message = self._p_messages.show(id_) # Get the message with the given ID
        print(f"Message: {message}")
        if message is None:
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        else:
            text_control = control.get_security_level(message) # Get the message security level
            if text_control is None or not control.is_authorized(self._user_level, text_control, "read"): # Check if the user is authorized to read the message
                print(f"ERROR! You are not authorized to read message ID \'{id_}\'")
            else:
                message.display_text()
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 

    def display(self):
        print("Messages:")
        self._p_messages.display(self._user_level)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_line("message"),
        self._username,
        self._prompt_for_line("date"))

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        self._p_messages.update(id_, self._prompt_for_line("message"))
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        self._p_messages.remove(self._prompt_for_id("delete"))

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ################################################## 
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ################################################## 

    def authenticate(self, username, password):  # Changed here
        id_ = self._id_from_user(username)
        if ID_INVALID != id_ and password == users[id_].password:
            return control.get_security_level(users[id_]) # Return the user's security level
        else:
            return None
    
    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ################################################## 
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID

    #####################################################
    # INTERACT :: DISPLAY USERS
    # Display the set of users in the system
    #####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
