"""
Objective :
-Wellcome page for user
-Register user to student
-Create common profile for student
-del student acc
-modify student info



"""
import copy

COMMANDS = ("me", "board", "remove", "quit")

students = {
   1: {
        "name": "John Doe",
        "marks": [4, 5, 1, 4, 5, 2, 5],
        "info": "John is 22 y.o. Hobbies: music",
    },
    2: {
        "name": "Marry Black",
        "marks": [4, 1, 3, 4, 5, 1, 2, 2],
        "info": "John is 23 y.o. Hobbies: football",
    },
}
# ==================================================
# student activities
# ==================================================

def show_students():
    student_dict = copy.deepcopy(students)
    for id_, student in student_dict.items():
        print(f"[{id_}] {student['name']}: {round(sum(student['marks'])/len(student['marks']), 1)}")
def details_students(name):
    while True:
        show_in = input("If you want watch details enter student id or exit:")
        if show_in == "exit":
            profile(name)
            break
        elif int(show_in) in students.keys():
            detail_info = students[int(show_in)]
            print(f"ID:{show_in} "
                  f"\n Name: {detail_info['name']} "
                  f"\n All Marks:{detail_info['marks']} "
                  f"\n Info: {detail_info['info']} ")
            continue
        else:
            if show_in not in students.keys():
                print("Wrong ID")
            else:
                print("Wrong command")
                continue
def delete_students(name: str):
    confirm = input(f"{name} are you sure you want delete your acc?\n yes or no \n ")
    if confirm == "yes":
        del students[finder_id_(name)]
        print("Your acc deleted")
        welcome()
    elif confirm == "no":
        profile(name)
    elif confirm != "yes" or "no":
        delete_students(name)





# ==================================================
# id
# ==================================================
def add_student(name: str):
    # id giver
    b = i_d()
    students[b] = {"name": name, "marks": None, "info": None}

def finder_id_(name: str):
    for id_, student in students.items():
       if student["name"] == name:
           return id_

def i_d():
    #  id for new
    id_ = len(students) + 1
    while 'id_' in students:
        id_ = id_ + 1
    return id_

# ==================================================
# second menu
# ==================================================
def about_student(name : str):
    print("You can enter info about you or correct your marks!\n Available commands: info, mark, quit")
    while True:
        about_menu = input("Chose commands\n info, mark, quit:\n")
        if about_menu == "info":
            new_info = input("Write your info:")
            students[finder_id_(name)]["info"] = new_info
            print("Info is add")
        elif about_menu == "mark":
            new_marks = input("Write your mark like this:\n4,5,6,7,8,9,1\n")
            students[finder_id_(name)]["marks"] = [int(item) for item in new_marks.split(",")]
            print("Marks is add")
        elif about_menu == "quit":
            profile(name)
        else:
            print("Error command!")
            continue


def welcome():
    print(f"Welcome to the Digital jornal!")
    copy_database = copy.deepcopy(students)
    name = input("Enter your name or exit:")
    if name == "exit":
        print("See you next time!Bye")

    elif len(name) > 0:
        for id_, student in copy_database.items():
            if student["name"] == name:
                profile(name)
        else:
            add_student(name)
            profile(name)
    else:
        print("Inccorect name")


# ==================================================
# main
# ==================================================
def profile(name: str):
    print(f"Welcome to the your profile {name}! Available commands: {COMMANDS}")
    while True:
        student_input = input("Enter the command:")
        if student_input not in COMMANDS:
            print(f"Command {student_input} is not available.")
            continue
        elif student_input == "quit":
            welcome()
            break
        elif student_input == "board":
            show_students()
            details_students(name)
        elif student_input == "me":
            about_student(name)
        elif student_input == "remove":
            delete_students(name)


welcome()
