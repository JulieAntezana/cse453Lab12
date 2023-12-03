'''
To run tests with pytest, use the pytest command in the terminal:
pytest test_cases.py


All messages are accessible to all users. Any user can view any message  

All messages are accessible to all users. Any user can add any message  

All messages are accessible to all users. Any user can modify any message  

All messages are accessible to all users. Any user can delete any message  

Users of any security level are able to view all messages, even ones higher than their security clearance should allow (ie. Public,  Confidential, Privileged, Secret) 

Attacker can get access to users and passwords in the program  

Usernames are printed out when the program first starts  

Change FILE_NAME to upload a different messages file  

Alter messages.txt  

Alter list of usernames/passwords. This could include adding attacker as a user or denying access to legitimate users.  

Access any messages in system (there is no control currently working in the program to prevent anyone from logging in and viewing, modifying, deleting messages)  

Messages do not save who or when the message was edited  

There is no way to add or remove users. Public users are more like guest users.  

The program session does not expire after a set period of disuse  

 

All test cases should have an input, a name or scenario for the testcase, and an expected output. Above are example threats we gathered from the Week 09 Lab. 
'''

# import pytest
import interact
import messages
import message
import control

# Similar to the message program, this test set does not check access control, yet.

def test_login() -> dict:
    return {
        "name": "Login with valid username and password",
        "cases": {
            "AdmiralAbe": "ch0ppedLiver",
            "CaptainCharlie": "ch0ppedWood",
            "SeamanSam": "ch0ppedCelery",
            "SeamanSue": "Pa$$word",
            "SeamanSly": "password",
            "Murffkins": "password"
        },
        "expected": [
            "Invalid username or password.", # invalid login
            "Invalid username or password.", # invalid login
            "Invalid username or password.", # invalid login
            "Invalid username or password.", # invalid login
            "Welcome, SeamanSly. Please select an option:", # valid login
            "Invalid username or password." # invalid login
        ]        
    }


def test_update_delete_messages() -> dict: # Austin test cases
    return {
        "name": "Interact with Messages",
        "cases": {
            "SeamanSly": "password",
            "Murffkins": "password",
            "CaptainCharlie": "password",
            "AdmiralAbe": "password",
        },
        "expected": [
            {
                "login_result": "Welcome, ______. Please select an option:",
                "update_messages": [
                    ("99", "Invalid message ID. Please enter a valid ID."),
                    ("101", "Successfully updated message. Message ID '101'."),
                    ("", "Invalid message ID. Please enter a valid ID. ''."),
                    ("108", "SeamanSly = Message successfully updated, Murffkins = Unable to update message due to security level, CaptainCharlie = Message successfully updated, AdmiralAbe = Message successfully updated "),
                    ("105", "SeamanSly = Unable to update message due to security level, Murffkins = Unable to update message due to security level, CaptainCharlie = Message successfully updated, AdmiralAbe = Message successfully updated "),
                    ("109", "SeamanSly = Unable to update message due to security level, Murffkins = Unable to update message due to security level, CaptainCharlie = Unable to update message due to security level, AdmiralAbe = Message successfully updated "),
                ],
                "delete_messages": [
                    ("99", "Invalid message ID. Please enter a valid ID."),
                    ("101", "Successfully deleted message. Message ID '101'."),
                    ("", "Invalid message ID. Please enter a valid ID. ''."),
                    ("108", "SeamanSly = Message successfully deleted, Murffkins = Unable to delete message due to security level, CaptainCharlie = Message successfully deleted, AdmiralAbe = Message successfully deleted "),
                    ("105", "SeamanSly = Unable to delete message due to security level, Murffkins = Unable to delete message due to security level, CaptainCharlie = Message successfully deleted, AdmiralAbe = Message successfully deleted "),
                    ("109", "SeamanSly = Unable to delete message due to security level, Murffkins = Unable to delete message due to security level, CaptainCharlie = Unable to delete message due to security level, AdmiralAbe = Message successfully deleted "),
                ]
            },
            {
                "login_result": "Invalid username or password."
            }
        ]
    }


def login_test_generator(username, password):
    interact_ = interact.Interact(username, password, messages)
    if interact_.get_user_level() is None:
        return "Invalid username or password."
    return f"Welcome, {username}. Please select an option:"


# Write down access control
def test_add_message() -> dict:
    return {
        "name": "Write down access control",
        "cases": {
            "AdmiralAbe": "password",
            "CaptainCharlie": "password",
            "SeamanSam": "password",
            "SeamanSue": "password",
            "SeamanSly": "password",
            "Murffkins": "password"
        },
        "expected": [
            {

            }
        ]
    }

def add_test_generator(text, textControl, author):
    addMessage = messages.Messages.add(text, textControl, author):
    # if addMessage.textControl 

        # def add(self, text: str, text_control: control.Level, author: str, date):
            # m = message.Message(text, text_control, author, date)
            # self._messages.append(m)

def run_tests(test_set: dict):
    print("\n{}\n".format(test_set.get("name")))
    cases = test_set.get('cases')
    expected = test_set.get('expected')
    for i, (username, password) in enumerate(cases.items()):
        actual = login_test_generator(username, password)
        print("Expected:", expected[i])
        print("Actual:", actual)
        # Use a conditional expression to print "Pass" or "Fail"
        print("Result:", "Pass" if actual == expected[i] else "Fail")
        print("===================")

        #Murff
        actualAddMessage = add_test_generator()
        print("Expected:", expected[i])
        print("Actual:", actualAddMessage)
        # Use a conditional expression to print "Pass" or "Fail"
        print("Result:", "Pass" if actualAddMessage == expected[i] else "Fail")
        print("===================")

       
def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nRun Access Control sets of tests")
            run_tests(test_login())
            run_tests(test_add_message())
            # run_tests(test_union())
            # run_tests(test_additional_statement())
            # run_tests(test_comment())
            continue
        if choice == "h":
            print_menu()
            continue
        if choice == "q":
            break
        print("Invalid choice. Please make a choice from the available options.")


def print_menu():
    print("""
    1. Set of tests\n
    2. Set of Update/Delete tests\n
    h. Display menu\n
    q. Exit\n""")


if __name__ == "__main__":
    driver_program()
