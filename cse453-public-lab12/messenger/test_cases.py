'''
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
import main
import interact
import messages
import message
import control

# Similar to the message program, this test set does not check access control, yet.
def test_login() -> dict:
    return {
        "name": "Login with valid username and password",
        "cases": {
            "AdmiralAbe": "password",
            "CaptainCharlie": "password",
            "SeamanSam": "password",
            "SeamanSue": "password",
            "SeamanSly": "password",
            "Murffkins": "password"
        },
        "expected": "Welcome, {username}. Please select an option: "
    }

# def test_view_messages() -> dict:
#     return {
#         "name": "Valid user can view list of message properties",
#         "cases": {
#             "AdmiralAbe": "Password",
#             "CaptainCharlie": "password",
#             "SeamanSam": "password",
#             "SeamanSue": "password",
#             "SeamanSly": "password",
#             "Murffkins": "password"
#         },
#         "expected": message.display_properties(message)
#     }

def login_test_generator(username, password):
    interact_ = interact.Interact(username, password, messages)
    return interact_ # return the Interact object

def run_tests(test_set: dict):
    print("\n{}\n".format(test_set.get("name")))
    cases = test_set.get('cases')
    for username, password in cases.items():
        expected = test_set["expected"].format(username=username)
        actual = login_test_generator(username, password)
        print("Expected:", expected)
        print("Actual:", f"Welcome, {actual._username}. Please select an option:\n")
        print("===================")
        
def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nRun Access Control sets of tests")
            run_tests(test_login())
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
        print("Invalid choice. Please chose out of available.")


def print_menu():
    print("""
    1. Set of tests\n
    h. Display menu\n
    q. Exit\n""")


if __name__ == "__main__":
    driver_program()
