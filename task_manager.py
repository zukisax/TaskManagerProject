#=====importing libraries===========
'''This is the section where you will import libraries'''
import math
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your username and password
'''
# Create an empty list's to store usernames and passwords from the text file
usernames = []
passwords = []
# Read the usernames and passwords from the "user.txt" file
with open("user.txt","r") as rfile:
    for line in rfile:
        new_line = line.strip()
        new_line = new_line.split(", ")
        # Append elements of list "new_line" into "usernames" and "passwords"
        usernames.append(new_line[0])
        passwords.append(new_line[1])

# Log-in section exits the program when either log-in input is incorrect!
print("kindly prepare to log-in with your credentials!")
login_username = input("Enter your log-in username: ").lower()
if login_username not in usernames:
    print("Invalid input: log-in username is incorrect!")
    exit()

login_password = input("Enter your log-in password: ").lower()
print("")
if login_password not in passwords:
    print("Invalid input: log-in password is incorrect!")
    exit()

elif login_password in passwords:
    # Validate the username and password, with a while loop structure
    index = 0
    while index < len(usernames):
        print(f"The user: {usernames[index]} has the password: {passwords[index]}")
        index += 1

##############################################################################
print("")
while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vs - view statistics                 
e - exit
: ''').lower()

    if menu == 'r':

        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        print("")
        # Ensure only the username admin is allowed to register users
        # Create new variable super_user, to store admin username

        # Only the admin can register a new user
        super_user_name = input("Admin please enter your username: ").lower()
        if super_user_name != "admin":
            print("Invalid input: only admin can register new users!")
            continue
        
        # Eliminate duplication of usernames in user.txt
        user_name = input("Please enter the new username: ").lower()
        if (user_name in usernames): 
            print("\nInvalid input: username already exists!")
            print("")
            continue

        # Eliminate duplication of passwords in user.txt
        pass_word = input("Please enter the new password: ").lower()
        if (pass_word in passwords): 
            print("\nInvalid input: password already exists!")
            continue    

        # New user password confirmation
        pass_word_conf = input("Please confirm the new password: ").lower()    
        if pass_word_conf != pass_word:
            print("\nInvalid input: password confirmation is incorrect!")
            print("")
            continue

        else:
            with open("user.txt", "a") as wfile:
                wfile.write(f"\n{user_name}, {pass_word}")    
        
    #########################################################################

    elif menu == 'a':
        #pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        print("")
        username = input("Enter the username assigned to the task: ").lower()
        title_task = input("Enter the title of the task: ")
        description_task = input("Enter the description of the task: ")
        date_assigned = str(datetime.date.today())
        date_due = str(datetime.date.today() + datetime.timedelta(10))
        task_completed = "No"

        # Exclude users not in the input file user.txt
        if username not in usernames:
            print("\nInvalid input: username does not exist!")
            print("")
            continue            

        # Create a string list "task_list" to store the above input data
        task_list = ["str"]*6
        task_list[0] = username
        task_list[1] = title_task
        task_list[2] = description_task
        task_list[3] = date_assigned
        task_list[4] = date_due
        task_list[5] = task_completed

        # Write the data about the task to the file "tasks.txt"
        with open("tasks.txt", "a") as wfile_a:
            wfile_a.write(f"\n{task_list[0]}, {task_list[1]}, {task_list[2]}, {task_list[3]}, {task_list[4]}, {task_list[5]}")
    #########################################################################################################################

    elif menu == 'va':
        #pass
        print("")
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        # Read the file "tasks.txt" with a use of a for loop struture   
        with open("tasks.txt", "r") as rfile_va:
            for task_va in rfile_va:
                new_task_va = task_va.strip()
                new_task_va = new_task_va.split(", ")
                
                # Display information on each task in an easy-to-read format
                print("Task:                     ",new_task_va[1])
                print("Assigned to:              ",new_task_va[0])
                print("Date assigned:            ",new_task_va[3])
                print("Date date:                ",new_task_va[4])
                print("Task Complete?            ",new_task_va[5])
                print("Task Description:         ",new_task_va[2])
                print("")
    ########################################################################
                            
    elif menu == 'vm':
        #pass
        print("")
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        # Request the username of the current user
        username_vm = input("Enter username of the current user: ").lower()

        # Exclude users not in the input file user.txt
        if username_vm not in usernames:
            print("Invalid input: username does not exist!")
            print("")
            continue

        with open("tasks.txt", "r") as rfile_vm:
            for task_vm in rfile_vm:
                new_task_vm = task_vm.strip()
                new_task_vm = new_task_vm.split(", ")
                
                # Choose the current user
                if username_vm == new_task_vm[0]:
                    # Display user information in an easy-to-read format
                    print("Task:                     ",new_task_vm[1])
                    print("Assigned to:              ",new_task_vm[0])
                    print("Date assigned:            ",new_task_vm[3])
                    print("Date date:                ",new_task_vm[4])
                    print("Task Complete?            ",new_task_vm[5])
                    print("Task Description:         ",new_task_vm[2])
                    print("")

    #########################################################################
    elif menu == 'vs':
        print("")
        # Request the username of the administrator
        username_vs = input("Enter username of the administator: ").lower()

        # Ensure the administrator is the one running the statistics
        if username_vs != 'admin':
            print("Invalid input: user is not admin!")
            print("")
            continue

        # Open user.txt and count the number of users with a for loop
        with open("user.txt", "r") as rfile_vs_user:
            num_users = 0
            for user_vs in rfile_vs_user:
                num_users += 1
            print(f"The total number of users: {num_users}")

        # Open tasks.txt and count the number of tasks with a for loop
        with open("tasks.txt", "r") as rfile_vs_task:
            num_tasks = 0
            for task_vs in rfile_vs_task:
                num_tasks += 1
            print(f"The total number of tasks: {num_tasks}")            

    ########################################################################
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    #########################################################################
    else:
        print("You have entered an invalid input. Please try again")


# References
# 1) https://www.youtube.com/watch?v=tlmOm35lsps
# 2) https://www.youtube.com/watch?v=BRrem1k3904&t=1s
# 3) https://www.youtube.com/watch?v=Uh2ebFW8OYM&t=104s
# 4) https://www.youtube.com/watch?v=0HaYhgKba9c&t=2s

