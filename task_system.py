from task_functions import *

def main():
    # Define the priority scale
    priority_map = {
        1: "Highest",
        2: "High",
        3: "Medium",
        4: "Low",
        5: "Lowest"
    }

    # Initialize the list of tasks
    all_tasks = []

    # Define the main menu options
    main_menu = {
    'V': "View tasks",
    'A': "Add new task",
    'D': "Delete a task",
    'C': "Change task status",
    'U': "Update task fields",
    'S': "Save tasks to a file",
    'L': "Load tasks from a file",
    'Q': "Quit"
    }   

    # Main loop
    while True:
        print_main_menu(main_menu)
        option = input("Enter your selection: ")
        option = option.upper()
        if option == 'Q':
            print("Exiting program.")
            break
        main_menu_actions(option, all_tasks, priority_map)

if __name__ == '__main__':
    main()