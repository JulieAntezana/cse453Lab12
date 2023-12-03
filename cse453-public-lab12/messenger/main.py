########################################################################
# Program:
#    Lab 12, Bell-LaPadula
# Author:
#    Br. Helfrich, Kyle Mueller, Nicholas Balabanov
# Summary: 
#    This program is designed to keep track of a number of secret
#    messages. IT will display messages to the appropriate users
#    and withhold messages from those lacking the authority.
########################################################################

from os import path
import interact
import messages

# Gets the absolute path of the "messages.txt" file
FILE_NAME = path.join(path.dirname(path.abspath(__file__)), "messages.txt")

session_open = True


def close_session():
    global session_open
    session_open = False


def open_session():
    global session_open
    session_open = True


################################################
# DISPLAY OPTIONS
################################################
def display_options():
    print("\td .. Display the list of messages\n" +
          "\tdu .. Display the list of users\n" +
          "\tau .. Add user to the list\n" +
          "\tru .. Remove user from list\n" +
          "\tpp .. Promote user privileges \n" +
          "\tdp .. Demote user privileges\n" +
          "\ts .. Show one message\n" +
          "\ta .. Add a new message\n" +
          "\tu .. Update an existing message\n" +
          "\tr .. Delete an existing message\n" +
          "\to .. Display this list of options\n" +
          "\tl .. Log out\n")


################################################
# SIMPLE PROMPT
################################################
def simple_prompt(prompt):
    return input(prompt)


####################################################
# SESSION
# One login session
####################################################
def session(messages):
    open_session()

    print("Users:")
    interact.display_users()
    username = simple_prompt("\nWhat is your username? ")
    password = simple_prompt("What is your password? ")
    interact_ = interact.Interact(username, password, messages)
    if interact_.get_user_level() is None:
        print("Invalid username or password.")
        return

    print(f"\nWelcome, {username}. Please select an option:\n")
    display_options()

    while session_open:
        option = input(f"{username}> ")
        if option == "o":
            print('Options:')
            display_options()
        if option == "du":
            interact.display_users(interact_.get_auth())
        elif option == "d":
            interact_.display()
        elif option == "s":
            interact_.show()
        elif option == "a":
            interact_.add()
        elif option == "au":
            interact_.add_user()
        elif option == "u":
            interact_.update()
        elif option == "pp":
            interact_.promote_user()
        elif option == "dp":
            interact_.demote_user()
        elif option == "r":
            interact_.remove()
        elif option == "ru":
            interact_.remove_user()
        elif option == "l":
            print(f'Goodbye, {username}{chr(10)}')
            close_session()


####################################################
# MAIN
# Where it all begins and where it all ends
####################################################
def main():
    messages_ = messages.Messages(FILE_NAME)

    done = False
    while not done:
        session(messages_)
        done = input("Will another user be logging in? (y/n) ").upper() != "Y"

    return 0


if __name__ == "__main__":
    main()
