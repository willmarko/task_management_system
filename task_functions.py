import csv
import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print(f"==========================\nWhat would you like to do?")
    for key in menu:
        print(f"{key} - {menu[key]}")
    print("==========================")

def get_written_date(date_list):
    """
    The function ...
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    # Finish the function
    date = f"{month_names[int(date_list[0])]} {int(date_list[1])}, {date_list[2]}"
    # Return the date string in written format
    return date

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper=True, go_back=False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from.
    Asks the user to select an option using the input() function.
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper()  # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection].lower()}|.")
    return selection

def print_task(task, priority_map):
    for key, value in task.items():
        if key == 'priority':
            priority = priority_map.get(value, 'Unknown')  # Use 'Unknown' if priority value is not found in the map
            print(f"{key}: {priority}")
        else:
            print(f"{key}: {value}")

def print_tasks(tasks, priority_map, filter_option=None, show_idx=False, start_idx=1):
    """
    param: tasks (list) - a list of tasks to print
    param: priority_map (dict) - a dictionary mapping priority values
            to their representations
    param: filter_option (string) - an optional filter option to display
            only completed or incomplete tasks
    param: show_idx (bool) - a flag indicating whether to show task indices
    param: start_idx (int) - the starting index for task enumeration

    The function prints the tasks based on the given parameters.
    If a filter_option is provided, it displays only completed or
    incomplete tasks. If show_idx is True, it shows the task indices.
    The start_idx parameter sets the initial index for task enumeration.
    """
    filtered_tasks = []
    if filter_option == 'C':
        filtered_tasks = [task for task in tasks if task.get('done', '') == 'yes']
    elif filter_option == 'I':
        filtered_tasks = [task for task in tasks if task.get('done', '') == 'no']
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks to display.")
        return

    for idx, task in enumerate(filtered_tasks, start=start_idx):
        if show_idx:
            print(f"{idx}: ", end='')
        print_task(task, priority_map)

def is_valid_index(idx, in_list, start_idx=1, return_task=True):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that the provided index
    idx is a valid positive index that can retrieve
    an element from in_list.

    returns:
    - True, if idx is a positive numeric index
    that can retrieve an element from in_list.
    - False if idx is not an integer value, is negative
    or exceeds the size of in_list.
    """
    if type(idx) == str and type(in_list) == list and type(start_idx) == int:
        if start_idx > int(idx):
            return False
        else:
            if idx.isdigit() == True and abs(int(idx)) >= 0 and (int(idx) - start_idx) < len(in_list):
                return True
            else:
                return False
    else:
        return False

def delete_item(info_list, idx, start_idx=0):
    """
    param: info_list - a list from which to remove
            an item
    param: idx (str) - a string that is expected to
            contain an integer index of an item in
            the in_list
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function first checks if info_list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from info_list.

    returns:
    If info_list is empty, return 0.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from info_list.

    Helper functions:
    - is_valid_index()
    """
    if info_list == []:
        return None
    if is_valid_index(idx, info_list, start_idx):
        return info_list.pop(int(idx) - start_idx)
    return None

def is_valid_name(name_str):
    """
    param: name_str - a string containing the inputed
    wanted task name

    The function first checks if name_str is of type str.
    If so, the function then checks whether name_str's
    length is between 3 and 25 characters.

    returns:
    If name_str passes the validations, return True
    Otherwise, return False
    """
    if type(name_str) == str:
        if 3 <= len(name_str) <= 25:
            return True
    return False

def is_valid_priority(prio_str, prio_dict):
    """
    param: prio_str - a string containing the inputed
    priority value

    param: prio_dict - a dictionary with key values
    associating priority values with the level of priority

    The function first checks that our two arguments are
    of the right types. If so, the function use .isdigit()
    to confirm that prio_str is a str containing a valid integer.
    If true, the final validation checks whether the integer
    stored in prio_str is a key value in our prio_dict

    returns:
    If all validations are passed, return True
    Otherwise, return False
    """
    if prio_str == '':
        return False
    else:
        if type(prio_str) == str and type(prio_dict) == dict:
            if (prio_str.strip()).isdigit() == True:
                if int(prio_str) in prio_dict:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

def is_valid_month(date_list):
    """
    param: date_list - a list containing 3 elements

    The function takes a list, date_list (which has 3 elements)(month, day, and year)
    and first confirms that they are all integers stored in a string, and then determines
    whether date_list[0] our month is between the valid month values of 1 and 12 (inclusive)

    returns:
    True if all validations are passed
    Otherwise, return False
    """
    if str(date_list[0]).isdigit() and str(date_list[1]).isdigit() and str(date_list[2]).isdigit():
        if 1 <= int(date_list[0]) <= 12:
            return True
        else:
            return False
    else:
        return False

def is_valid_day(date_list):
    """
    param: date_list - a list containing 3 elements

    The function takes a list, date_list (which has 3 elements)(month, day, and year)
    and first confirms that they are all integers stored in a string, and then determines
    whether date_list[1] our day is between the valid day values for its associated month
    date_list[0] using our dictionary num_days

    returns:
    True if all validations are passed
    Otherwise, return False
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if is_valid_month(date_list):
        if int(date_list[1]) <= num_days[int(date_list[0])]:
            return True
        else:
            return False
    else:
        return False

def is_valid_year(date_list):
    """
    param: date_list - a list containing 3 elements

    The function takes a list, date_list (which has 3 elements)(month, day, and year)
    and first confirms that they are all integers stored in a string, and then determines
    whether date_list[2] our year a valid year (greater than 1000)

    returns:
    True if all validations are passed
    Otherwise, return False
    """
    if int(date_list[2]) >= 1000:
        return True
    else:
        return False

def is_valid_date(date_str):
    """
    param: date_str - a string containing a date in format (mm/dd/yyyy)

    The function first confirms date_str is of type str, if so, it then
    takes the string, breaks it into a list containing 3 elements, by using .split("/")
    and runs each of the helper functions on our list to confirm date_str has a valid month, day, and year

    returns:
    True if all validations are passed
    Otherwise, return False

    helper functions:
    is_valid_month
    is_valid_day
    is_valid_year
    """
    if type(date_str) == str:
        if is_valid_index("2", date_str.split("/"), 0) == False:
            return False
        else:
            if is_valid_month(list(date_str.split("/"))) == True and is_valid_day(list(date_str.split("/"))) == True and is_valid_year(list(date_str.split("/"))) == True:
                return True
            else:
                return False
    else:
        return False

def is_valid_completion(complete_str):
    """
    param: complete_str - a string containing the inputted completion status

    The function first confirms that complete_str is of type str, if so,
    it checks that complete_str contains exactly (case-sensitive) either "yes" or "no"

    returns:
    True if complete_str contains either "yes" or "no"
    Otherwise, return False
    """
    if type(complete_str) == str:
        if complete_str == 'yes' or complete_str == 'no':
            return True
        else:
            return False
    else:
        return False

def get_new_task(task_data, priority_map):
    """
    param: list - a list containing

    param: dictionary - a dictionary with priority scale for our is_valid_priority function

    The function first confirms that our list has 5 elements in it. If not,
    our function wil stop and return the length of the given list. Otherwise, we move on and
    the function confirms that each element within our list is of type str. If not, our function
    will stop and return ("type", and the list element that did not pass the str validation).
    Otherwise, we move on and check that each element of our list is a valid input using each
    helper function for the associated element, if any fail our function will return
    ("which element type failed", and the input it had). Otherwise if all validations were True
    and passed, get_new_task will return a dictionary with each of the listed elements inside
    and linked with their associated key value.

    helper functions:
    is_valid_name
    is_valid_priority
    is_valid_date
    is_valid_completion
    """
    if len(task_data) != 5:
        return len(task_data)
    name, info, priority, due_date, done = task_data
    if is_valid_name(name) and is_valid_priority(priority, priority_map) and \
        is_valid_date(due_date) and is_valid_completion(done):
        task = {
            'name': name,
            'info': info,
            'priority': int(priority),
            'duedate': due_date.strip(),
            'done': done.strip()
        }
        return task
    else:
        return None

def load_tasks_from_csv(filename, all_tasks, priority_scale):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            all_tasks.clear()  # Clear existing tasks before loading from CSV
            for row in reader:
                task = {
                    'name': row.get('name', ''),
                    'info': row.get('info', ''),
                    'priority': int(row.get('priority', 0)),
                    'duedate': row.get('duedate', ''),
                    'done': row.get('done', '')
                }
                all_tasks.append(task)

        return []
    except FileNotFoundError:
        return None

def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    if filename[-4:] != ".csv":
        return -1
    else:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for task in tasks_list:
                csv_writer.writerow(list(task.values()))
        return None

def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    if type(info_list) == list and type(idx) == str and type(start_idx) == int and type(priority_map) == dict and type(field_key) == str and type(field_info) == str:
        if info_list == []:
            return 0
        if is_valid_index(idx, info_list, start_idx) == False:
            return -1
        if field_key in info_list[int(idx.strip())] == False:
            return -2
        if len(info_list) > 0 and is_valid_index(idx, info_list, start_idx) == True and field_key in info_list[int(idx)]:
            if field_key == "name" and is_valid_name(field_info) == True:
                (info_list[int(idx)-start_idx])[field_key] = field_info
                return info_list[int(idx)-start_idx]
            if field_key == "info":
                (info_list[int(idx)-start_idx])[field_key] = field_info
                return info_list[int(idx)-start_idx]
            if field_key == "priority" and is_valid_priority(field_info, priority_map) == True:
                (info_list[int(idx)-start_idx])[field_key] = field_info
                return info_list[int(idx)-start_idx]
            if field_key == "duedate" and is_valid_date(field_info) == True:
                (info_list[int(idx)-start_idx])[field_key] = field_info
                return info_list[int(idx)-start_idx]
            if field_key == "done" and is_valid_completion(field_info) == True:
                (info_list[int(idx)-start_idx])[field_key] = field_info
                return info_list[int(idx)-start_idx]
        else:
            return field_key
    else:
        return field_key

def save_tasks_to_csv(tasks, filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "info", "priority", "duedate", "done"])
            for task in tasks:
                writer.writerow([task.get('name', ''),
                                 task.get('info', ''),
                                 task.get('priority', ''),
                                 task.get('duedate', ''),
                                 task.get('done', '')])
        return None
    except Exception as e:
        return str(e)

def restore_tasks_from_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            tasks = []
            header = next(reader)  # Skip the header row
            for row in reader:
                task = {
                    'name': row[0],
                    'info': row[1],
                    'priority': int(row[2]),
                    'duedate': row[3],
                    'done': row[4]
                }
                tasks.append(task)
        return tasks
    except FileNotFoundError:
        return None

def main_menu_actions(option, all_tasks, priority_map):
    """
    param: option (string) - a letter that the user selected from the menu
    param: all_tasks (list) - a list that contains dictionaries with tasks
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")

    The function performs the requested action based on the user's input.
    For each possible value of the option, the function either displays
    the tasks, prompts the user to add a new task, deletes a task,
    changes the status of a task, updates other fields of a task,
    or saves and loads tasks to/from a CSV file.

    returns: None
    """
    if option == 'V':
        # Display tasks
        clear_screen()
        view_options = {
            'A': 'All tasks',
            'C': 'Completed tasks',
            'I': 'Incomplete tasks'
        }
        view_option = get_selection("view", view_options)
        clear_screen()
        print(f"::: {view_options[view_option]}:")
        print_tasks(all_tasks, priority_map, filter_option=view_option, show_idx=True, start_idx=1)
    elif option == 'A':
        # Add a new task
        clear_screen()
        print("::: Add a new task (info can be left blank):")
        task_data = []
        field_names = ['name', 'info', 'priority', 'duedate', 'completion status (yes or no)']
        for field in field_names:
            field_value = input(f"Enter the {field}: ")
            task_data.append(field_value)
        new_task = get_new_task(task_data, priority_map)
        if new_task is not None:
            all_tasks.append(new_task)
            print("New task added successfully!")
        else:
            print("Invalid task data. Task not added.")
    elif option == 'D':
        # Delete a task
        clear_screen()
        print("::: Delete a task:")
        idx = input("Enter the index of the task you want to delete: ")
        if is_valid_index(idx, all_tasks, start_idx=1):
            deleted_task = delete_item(all_tasks, idx, start_idx=1)
            if deleted_task is not None:
                print("Task deleted successfully:")
                print_task(deleted_task, priority_map)
            else:
                print("Invalid index. Task not deleted.")
        else:
            print("Invalid index. Task not deleted.")
    elif option == 'C':
        # Change task status
        clear_screen()
        print("::: Change task status:")
        idx = input("Enter the index of the task you want to change status for: ")
        if is_valid_index(idx, all_tasks, start_idx=1):
            task = all_tasks[int(idx) - 1]
            print("Current task status:")
            print_task(task, priority_map)
            new_status = input("Enter the new status (yes or no): ")
            if is_valid_completion(new_status):
                task['done'] = new_status
                print("Task status updated successfully!")
            else:
                print("Invalid status. Task status not updated.")
        else:
            print("Invalid index. Task status not updated.")
    elif option == 'U':
        # Update task fields
        clear_screen()
        print("::: Update task fields:")
        idx = input("Enter the index of the task you want to update: ")
        if is_valid_index(idx, all_tasks, start_idx=1):
            task = all_tasks[int(idx) - 1]
            print("Current task:")
            print_task(task, priority_map)
            field = input("Enter the field you want to update (name, info, priority, duedate, done): ")
            if field == 'name':
                new_value = input("Enter the new name: ")
                task['name'] = new_value
            elif field == 'info':
                new_value = input("Enter the new info: ")
                task['info'] = new_value
            elif field == 'priority':
                new_value = input("Enter the new priority: ")
                if is_valid_priority(new_value, priority_map):
                    task['priority'] = int(new_value)
                else:
                    print("Invalid priority value. Task not updated.")
            elif field == 'duedate':
                new_value = input("Enter the new due date: ")
                if is_valid_date(new_value):
                    task['duedate'] = new_value
                else:
                    print("Invalid due date format. Task not updated.")
            elif field == 'done':
                new_value = input("Enter the new completion status (yes or no): ")
                if is_valid_completion(new_value):
                    task['done'] = new_value
                else:
                    print("Invalid completion status. Task not updated.")
            else:
                print("Invalid field. Task not updated.")
        else:
            print("Invalid index. Task not updated.")
    elif option == 'S':
        # Save tasks to a CSV file
        clear_screen()
        filename = input("Enter the filename to save tasks to (must end in .csv): ")
        save_result = save_tasks_to_csv(all_tasks, filename)
        if save_result is None:
            print("Tasks saved successfully!")
        else:
            print(f"Error saving tasks: {save_result}")
    elif option == 'L':
        # Load tasks from a CSV file
        clear_screen()
        filename = input("Enter the filename to load tasks from (must end in .csv): ")
        load_result = load_tasks_from_csv(filename, all_tasks, priority_map)
        if load_result is None:
            print(f"Error loading tasks: {load_result}")
        else:
            print("Tasks loaded successfully!")
    else:
        clear_screen()
        print("Invalid option. Please select a valid option.")