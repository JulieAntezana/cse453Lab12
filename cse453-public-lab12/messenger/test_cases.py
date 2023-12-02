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


def test_update_delete_messages() -> dict: # Austin
    return {
        "name": "Interact with Messages",
        "cases": {
            "SeamanSly": "password",
            "Murffkins": "password"
        },
        "expected": [
            {
                "login_result": "Welcome, SeamanSly. Please select an option:",
                "update_messages": [
                    ("1", "Invalid message ID. Please enter a valid ID."),
                    ("2", "Invalid message ID. Please enter a valid ID."),
                    ("3", "Invalid message ID. Please enter a valid ID."),
                    ("100", "Invalid message ID. Please enter a valid ID."),
                    ("1", "Failed to update message. Message ID '100' does not exist."),
                    ("2", "Failed to update message. Message ID '100' does not exist."),
                    ("3", "Failed to update message. Message ID '100' does not exist."),
                    ("1", "Successfully updated message. Message ID '1'."),
                    ("2", "Successfully updated message. Message ID '2'.")
                ],
                "delete_messages": [
                    ("1", "Invalid message ID. Please enter a valid ID."),
                    ("2", "Invalid message ID. Please enter a valid ID."),
                    ("3", "Invalid message ID. Please enter a valid ID."),
                    ("100", "Invalid message ID. Please enter a valid ID."),
                    ("1", "Failed to delete message. Message ID '100' does not exist."),
                    ("2", "Failed to delete message. Message ID '100' does not exist."),
                    ("3", "Failed to delete message. Message ID '100' does not exist."),
                    ("1", "Successfully deleted message. Message ID '1'."),
                    ("2", "Successfully deleted message. Message ID '2'.")
                ]
            },
            {
                "login_result": "Invalid username or password."
            }
        ]
    }


# Austins run update/delete function
def run_update_delete_tests(test_set: dict):
    print("\n{}\n".format(test_set.get("name")))
    cases = test_set.get('cases')
    expected = test_set.get('expected')

    for i, (username, password) in enumerate(cases.items()):
        interact_ = interact.Interact(username, password, messages.Messages("messages.txt"))
        actual_login_result = login_test_generator(username, password)
        print(f"Login Result: {actual_login_result}")

        if actual_login_result == expected[i]["login_result"]:
            print("Login Test: Pass\n")

            for j, (update_msg_input, update_msg_expected) in enumerate(expected[i]["update_messages"]):
                actual_update_result = interact_.update()
                print(f"Update Message Test {j + 1}: {actual_update_result}")
                assert actual_update_result == update_msg_expected

            for j, (delete_msg_input, delete_msg_expected) in enumerate(expected[i]["delete_messages"]):
                actual_delete_result = interact_.delete_message(int(delete_msg_input))
                print(f"Delete Message Test {j + 1}: {actual_delete_result}")
                assert actual_delete_result == delete_msg_expected

        else:
            print("Login Test: Fail\n")




def login_test_generator(username, password):
    interact_ = interact.Interact(username, password, messages)
    if interact_.get_user_level() is None:
        return "Invalid username or password."
    return f"Welcome, {username}. Please select an option:"

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
       
def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nRun Access Control sets of tests")
            run_tests(test_login())
        elif choice == "2":
            print("\nRun Update/Delete sets of tests")
            run_update_delete_tests(test_update_delete_messages())
            # run_tests(test_tautology())
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
