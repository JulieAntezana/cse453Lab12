########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control
import message


##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES ITERATOR
    # Make messages iterable
    ##################################################

    def __iter__(self):
        return iter(self._messages)

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, user_level):
        for m in self._messages:
            if control.access_rights(user_level, m.get_security_level(), "read"):
                m.display_properties()

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.display_text()

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(text)

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id):
        message_to_be_deleted = None
        for m in self._messages:
            if m.get_id() == id:
                m.clear()
                message_to_be_deleted = m
        self._messages.remove(message_to_be_deleted)

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text: str, text_control: control.Level, author: str, date):
        m = message.Message(text, text_control, author, date)
        self._messages.append(m)

    def read_message(self, message_id):
        for m in self._messages:
            if m.get_id() == message_id:
                return m

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    lvl = control.parse_security_level(text_control)
                    self.add(text.rstrip('\r\n'), lvl, author, date)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
