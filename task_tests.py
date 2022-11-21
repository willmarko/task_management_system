from task_functions import *

# get_written_date Asserts
assert get_written_date(["01", "02", "2022"]) == 'January 2, 2022'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'
#--------------------------------------------------------------------------------------

# is_valid_name Asserts
assert is_valid_name("work") == True
assert is_valid_name("wo") == False
assert is_valid_name("way too long name that nobody would read") == False
#--------------------------------------------------------------------------------------

# is_valid_priority Asserts
priority_scale = {11: "The one and only"}
assert is_valid_priority('11', priority_scale) == True
assert is_valid_priority(11, priority_scale) == False
#--------------------------------------------------------------------------------------

# is_valid_date Asserts
assert is_valid_date("06/03/2002") == True
assert is_valid_date("12/33/2002") == False
assert is_valid_date("-12/30/2002") == False
assert is_valid_date(12/30/2002) == False
#--------------------------------------------------------------------------------------

# is_valid_completion Asserts
assert is_valid_completion("no") == True
assert is_valid_completion("yes") == True
assert is_valid_completion("No") == False
assert is_valid_completion("Yes") == False
#--------------------------------------------------------------------------------------

# is_valid_index Asserts
list = [1, 2, 3, 4]
assert is_valid_index("1", list) == True
assert is_valid_index("8", list) == False

# delete_items Asserts
all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
    }

]

empty_list = []
one_element = [1]
two_element = [1, 2]
assert delete_item(empty_list, "1") == 0
assert delete_item(one_element, "2") == -1
assert delete_item(one_element, "0") == 1
assert delete_item(two_element, "1") == 2

#--------------------------------------------------------------------------------------

# get_new_task Asserts
new_task_list = ["Destroy the ring", "Go to Mount Doom and throw it in", "5", "03/25/3019", "yes"]
new_task_list_fail_name = new_task_list[:]
new_task_list_fail_name[0] = 42
assert get_new_task(new_task_list_fail_name, priority_scale) == ("type", 42)
new_task_list_fail_name[0] = ("hello", "world")
assert get_new_task(new_task_list_fail_name, priority_scale) == ("type", ("hello", "world"))

new_task_list_fail_date = new_task_list[:]
new_task_list_fail_date[3] = 20
assert get_new_task(new_task_list_fail_date, priority_scale) == ("type", 20)
new_task_list_fail_date[3] = ("hello", "world")
assert get_new_task(new_task_list_fail_date, priority_scale) == ("type", ("hello", "world"))

#using an existing new_task_list
priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}
new_task_list_fail_completion = new_task_list[:]
new_task_list_fail_completion[4] = "Yes" # ensure case sensitive
assert get_new_task(new_task_list_fail_completion, priority_scale) == ("done", "Yes")
#--------------------------------------------------------------------------------------

# Restore Asserts
assert load_tasks_from_csv("fakefile", all_tasks, priority_scale) == -1
assert load_tasks_from_csv("fakefile.csv", all_tasks, priority_scale) == None
assert load_tasks_from_csv("single-task.csv", all_tasks, priority_scale) == []
assert load_tasks_from_csv("combined.csv", all_tasks, priority_scale) == [2, 4, 5, 6]
assert load_tasks_from_csv("missing-date.csv", all_tasks, priority_scale) == [1]
#--------------------------------------------------------------------------------------

# Save Asserts
assert save_tasks_to_csv(all_tasks, "my-tasks.csv") == None
assert save_tasks_to_csv(all_tasks, "fakefile") == -1
#--------------------------------------------------------------------------------------

# Update_task Asserts
info_list = []
three_elements = [1, 2, 3]
assert update_task(info_list, "0", priority_scale, 'name', 'hey', 1) == 0
assert update_task(three_elements, "5", priority_scale, 'name', 'hey', 1) == -1
assert update_task(all_tasks, "0", priority_scale, "book", "") == "book"
#--------------------------------------------------------------------------------------